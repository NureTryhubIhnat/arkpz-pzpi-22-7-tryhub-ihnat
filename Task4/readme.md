# IoT Health Monitoring Project

This project implements an IoT-based health monitoring system using an ESP32 microcontroller. The device measures and displays the following parameters:

1. **Environmental Temperature**: Captured using a DS18B20 temperature sensor.
2. **Heart Rate (Pulse)**: Measured via a pulse sensor.
3. **Step Count**: Calculated using an MPU6050 accelerometer and gyroscope.

Additionally, the collected data is sent to an MQTT broker for remote monitoring.

## Features
- **Real-time Data Display**: Shows temperature, heart rate, and step count on an OLED screen.
- **Step Detection**: Detects steps using accelerometer and gyroscope data.
- **Remote Data Transmission**: Sends data to an MQTT broker.

## Components Used

1. **Microcontroller**: ESP32
2. **Temperature Sensor**: DS18B20
3. **Pulse Sensor**: Generic pulse sensor
4. **Accelerometer & Gyroscope**: MPU6050
5. **Display**: OLED 128x64
6. **Wi-Fi Connectivity**: Built-in ESP32 module

## Libraries Required
Make sure to install the following libraries in your Arduino IDE:
- `Wire.h`: For I2C communication.
- `Adafruit_GFX.h` and `Adafruit_SSD1306.h`: For the OLED display.
- `DallasTemperature.h` and `OneWire.h`: For the DS18B20 temperature sensor.
- `Adafruit_MPU6050.h`: For MPU6050 sensor.
- `WiFi.h`: For Wi-Fi connectivity.
- `PubSubClient.h`: For MQTT communication.

## Setup
1. **Hardware Connections**:
   - **DS18B20 Sensor**: Connect to GPIO23.
   - **Pulse Sensor**: Connect to GPIO2.
   - **MPU6050**: Connect to the I2C pins (SDA and SCL).
   - **OLED Display**: Connect to the I2C pins (SDA and SCL).

2. **Wi-Fi Configuration**:
   Update the following lines in the code with your Wi-Fi credentials:
   ```cpp
   const char* ssid = "Your_SSID";
   const char* password = "Your_PASSWORD";
   ```

3. **MQTT Broker**:
   Configure the MQTT broker details:
   ```cpp
   const char* mqtt_server = "Your_MQTT_Broker_Address";
   const int mqtt_port = 1883;
   ```

## How It Works
1. The ESP32 initializes all connected sensors and establishes a connection to the MQTT broker.
2. Temperature is read from the DS18B20 sensor.
3. Heart rate is calculated using interrupts triggered by the pulse sensor.
4. Steps are detected based on motion thresholds from the MPU6050 sensor.
5. All data is displayed on the OLED screen and sent to the MQTT broker in JSON format:
   ```json
   {
     "temperature": 25.5,
     "steps": 120,
     "heartRate": 75
   }
   ```

## Usage
1. Upload the code to your ESP32 using the Arduino IDE.
2. Open the Serial Monitor to verify the Wi-Fi and MQTT connection.
3. View real-time data on the OLED display.
4. Monitor the transmitted data on your MQTT client.

## Future Enhancements
- Add more health metrics such as blood oxygen levels.
- Implement a mobile app for better visualization.
- Include battery monitoring for portability.

## License
This project is open-source and available under the MIT License.
