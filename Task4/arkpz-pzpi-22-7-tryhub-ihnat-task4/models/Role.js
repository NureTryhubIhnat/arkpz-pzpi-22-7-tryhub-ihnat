const { Schema, model } = require("mongoose");

const Role = new Schema({
  value: { type: String, unique: true, defualt: "USER" },
});

module.exports = model("Role", Role);
