require("dotenv").config();
const express = require("express");
const cors = require("cors");
const cookieParser = require("cookie-parser");
const mongoose = require("mongoose");
const router = require("./router/index");
const errorMiddleware = require("./middlewares/error-middleware");
const mqtt = require("mqtt");
const swaggerUi = require("swagger-ui-express");
const swaggerDocument = require("./swagger.json");
const Data = require("./models/Data.js");

const PORT = process.env.PORT || 5000;
const MQTT_BROKER = "mqtt://broker.hivemq.com"; // Broker's address
const MQTT_TOPIC = "iot/data"; // Topic for prepayment

const app = express();

// MongoDB model for storing data
const SensorData = mongoose.model(
  "SensorData",
  new mongoose.Schema({
    temperature: Number,
    steps: Number,
    heartRate: Number,
    timestamp: { type: Date, default: Date.now },
  })
);

// Swagger UI
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerDocument));
app.use(cookieParser());
app.use(express.json());
app.use(cookieParser());

app.use(
  cors({
    credentials: true,
    origin: process.env.CLIENT_URL,
  })
);

app.get("/", (req, res) => {
  res.send("Hello world");
});

app.use("/api", router);
app.use(errorMiddleware);

// Connect to an MQTT broker
const mqttClient = mqtt.connect(MQTT_BROKER);
mqttClient.on("connect", () => {
  console.log("MQTT connected");
  mqttClient.subscribe(MQTT_TOPIC, (err) => {
    if (err) {
      console.error("Помилка підписки на MQTT топік:", err);
    } else {
      console.log(`Підписка на топ ${MQTT_TOPIC} успішно оформлена.`);
    }
  });
});

mqttClient.on("message", async (topic, message) => {
  if (topic === MQTT_TOPIC) {
    const messageData = JSON.parse(message.toString());
    console.log(`Отримано повідомлення з топіка ${topic}: ${message.toString()}`);

    const { temperature, heartRate, steps } = messageData;

    // Создаем новый объект с данными для пользователя
    const data = new Data({
      userId: "67682ac15ab74a6348a0debc", // Привязываем данные к конкретному пользователю
      temperature,
      heartRate,
      steps,
    });

    try {
      // Сохраняем данные в базу данных
      await data.save();
      console.log("Дані успішно збережені у базі даних");
    } catch (err) {
      console.error("Помилка збереження даних:", err);
    }
  }
});

mqttClient.on("reconnect", () => {
  console.log("Connecting to MQTT...");
});

const start = async () => {
  try {
    await mongoose.connect(process.env.DB_URL, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    app.listen(PORT, () => console.log(`Server started on PORT = ${PORT}`));
  } catch (e) {
    console.log(e);
  }
};

start();
