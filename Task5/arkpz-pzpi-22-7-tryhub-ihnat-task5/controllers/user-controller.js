const userService = require("../service/user-service");
const { validationResult } = require("express-validator");
const ApiError = require("../exceptions/api-error");
const tokenService = require("../service/token-service");
const Data = require("../models/Data.js");
const User = require("../models/user-model.js");

class UserController {
  async registration(req, res, next) {
    try {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return next(ApiError.BadRequest("Validation error", errors.array()));
      }
      const { email, password, role } = req.body;

      const userData = await userService.registration(email, password, role);
      res.cookie("refreshToken", userData.refreshToken, {
        maxAge: 30 * 24 * 60 * 60 * 1000,
        httpOnly: true,
      });
      return res.json(userData);
    } catch (e) {
      next(e);
    }
  }

  async login(req, res, next) {
    try {
      const { email, password } = req.body;
      const userData = await userService.login(email, password);
      res.cookie("accessToken", userData.accessToken, {
        maxAge: 30 * 24 * 60 * 60 * 1000,
        httpOnly: true,
      });

      res.cookie("refreshToken", userData.refreshToken, {
        maxAge: 30 * 24 * 60 * 60 * 1000,
        httpOnly: true,
      });
      return res.json(userData);
    } catch (e) {
      next(e);
    }
  }

  async logout(req, res, next) {
    try {
      const { refreshToken } = req.cookies;
      const token = await userService.logout(refreshToken);
      res.clearCookie("refreshToken");
      res.clearCookie("accessToken");
      return res.json(token);
    } catch (e) {
      next(e);
    }
  }

  async activate(req, res, next) {
    try {
      const activationLink = req.params.link;
      await userService.activate(activationLink);
      return res.redirect(process.env.CLIENT_URL);
    } catch (e) {
      next(e);
    }
  }

  async refresh(req, res, next) {
    try {
      const { refreshToken } = req.cookies;
      const userData = await userService.refresh(refreshToken);
      res.cookie("refreshToken", userData.refreshToken, {
        maxAge: 30 * 24 * 60 * 60 * 1000,
        httpOnly: true,
      });
      return res.json(userData);
    } catch (e) {
      next(e);
    }
  }

  async getMyHealthData(req, res, next) {
    //
    try {
      const accessToken = req.cookies.accessToken; // Retrieving the token from cookies
      console.log(accessToken);
      const userData = tokenService.validateAccessToken(accessToken); // Validate the token
      console.log(userData);

      const userId = userData.id;

      console.log(userId);

      const userDataExists = await Data.find({ userId });
      let sumTemp = 0;
      let sumPulse = 0;
      let sumSteps = 0;

      if (userDataExists) {
        for (let i = 0; i < userDataExists.length; i++) {
          sumTemp += userDataExists[i].temperature;
          sumPulse += userDataExists[i].heartRate;
          sumSteps += userDataExists[i].steps;
        }
        const { email } = await User.findById(userId);

        const data = {
          messageTemp: `Average temperature for user with ID - ${userId} is ${sumTemp / userDataExists.length} `,
          messageHeartRate: `Average pulse for user with ID - ${userId} is ${sumPulse / userDataExists.length} `,
          messageSteps: `Average steps for user with ID - ${userId} is ${sumSteps / userDataExists.length} `,
          userEmail: email,
        };
        res.status(200).json(data);
      } else {
        console.log("No data found for the given user ID.");
      }
    } catch (e) {
      next(e);
    }
  }
}

module.exports = new UserController();
