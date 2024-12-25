#include <Wire.h>                   // I2C Library
#include <Adafruit_GFX.h>            // OLED Library
#include <Adafruit_SSD1306.h>        // OLED Library
#include <DallasTemperature.h>       // Temperature sensor Library
#include <OneWire.h>                 // OneWire protocol Library
#include <Adafruit_MPU6050.h>        // MPU6050 Library
#include <WiFi.h>                    // Wi-Fi Library
#include <PubSubClient.h>            // MQTT Library

// OLED Display Settings
#define SCREEN_WIDTH 128    // OLED display width, in pixels
#define SCREEN_HEIGHT 64    // OLED display height, in pixels
#define OLED_RESET    -1    // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(OLED_RESET); // Declaring the display

// Accelerometer Settings
Adafruit_MPU6050 mpu;
sensors_event_t accelerometer, gyroscope, temp;
const float STEP_THRESHOLD = 1.5; // Adjust this value to fine-tune step detection
float accMag, gyroMag;
int stepCount = 0;

// Temperature Sensor Settings
#define ONE_WIRE_BUS 23         // Define pin for DS18B20 (GPIO23)
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature temperatureSensors(&oneWire);

// Pulse Generator Settings
#define PULSE_PIN 2            // Pulse generator pin (GPIO2)
#define SAMPLING_INTERVAL 1000 // Interval for sampling pulse
volatile uint16_t pulse;
uint16_t count;
float heartRate;

// Wi-Fi credentials
const char* ssid = "Wokwi-GUEST";  // Network SSID
const char* password = "";  // Network password

// MQTT Broker Settings
const char* mqtt_server = "broker.hivemq.com"; // Replace with your broker if needed
const int mqtt_port = 1883; // Default MQTT port
const char* mqtt_user = ""; // MQTT username (if needed)
const char* mqtt_password = ""; // MQTT password (if needed)
const char* mqtt_topic = "iot/data"; // Topic to publish data

WiFiClient espClient;
PubSubClient mqttClient(espClient);

// Interrupt function for pulse generator
void HeartRateInterrupt() {
  pulse++;
}

void setup() {
  Serial.begin(115200);

  // Setup OLED display
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("OLED display not found!"));
    while (true);
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }

  // Initialize sensors
  temperatureSensors.begin();
  if (!mpu.begin()) {
    Serial.println("MPU6050 Error!");
    while (true);
  }

  pinMode(PULSE_PIN, INPUT);
  attachInterrupt(digitalPinToInterrupt(PULSE_PIN), HeartRateInterrupt, RISING);

  // Set up MQTT
  mqttClient.setServer(mqtt_server, mqtt_port);
  mqttClient.setCallback(mqttCallback);
  reconnectMQTT();
}

void loop() {
  // Ensure MQTT connection
  if (!mqttClient.connected()) {
    reconnectMQTT();
  }
  mqttClient.loop();

  static unsigned long startTime;
  if (millis() - startTime < SAMPLING_INTERVAL) {
    return;
  }
  startTime = millis();

  // Get temperature
  temperatureSensors.requestTemperatures();
  float temperature = temperatureSensors.getTempCByIndex(0);

  // Get heart rate
  count = pulse;
  pulse = 0;
  heartRate = map(count, 0, 220, 0, 220);

  // Get accelerometer readings
  mpu.getEvent(&accelerometer, &gyroscope, &temp);
  accMag = sqrt(sq(accelerometer.acceleration.x) + sq(accelerometer.acceleration.y) + sq(accelerometer.acceleration.z));
  gyroMag = sqrt(sq(gyroscope.gyro.x) + sq(gyroscope.gyro.y) + sq(gyroscope.gyro.z));

  // Detect steps
  if (accMag > STEP_THRESHOLD || gyroMag > STEP_THRESHOLD) {
    stepCount++;
  }

  // Display data on OLED
  display.clearDisplay();
  display.setCursor(0, 0);
  display.print("Temperature: ");
  display.print(temperature);
  display.println(" C");

  display.print("Pulse: ");
  display.print(heartRate);
  display.println(" BPM");

  display.print("Steps: ");
  display.println(stepCount);

  display.display();

  // Send data to MQTT
  sendDataToMQTT(temperature, stepCount, heartRate);
}

void sendDataToMQTT(float temperature, int steps, float heartRate) {
  String payload = "{\"temperature\": " + String(temperature) + 
                    ", \"steps\": " + String(steps) + 
                    ", \"heartRate\": " + String(heartRate) + "}";

  if (mqttClient.publish(mqtt_topic, payload.c_str())) {
    Serial.println("Data sent to MQTT: " + payload);
  } else {
    Serial.println("Failed to send data to MQTT.");
  }
}

// MQTT callback function
void mqttCallback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message received in topic: ");
  Serial.print(topic);
  String messageStr;
  for (int i = 0; i < length; i++) {
    messageStr += (char)message[i];
  }
  Serial.println(messageStr);
}

// Reconnect to MQTT broker
void reconnectMQTT() {
  while (!mqttClient.connected()) {
    if (mqttClient.connect("ESP32Client", mqtt_user, mqtt_password)) {
      mqttClient.subscribe(mqtt_topic);
    } else {
      delay(5000);
    }
  }
}
