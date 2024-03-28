# iot_core

Raspberry Pi Pico W - sensors setup for sending data through MQTT protocol to AWS IoT Core

## Lambda Folder

This folder contains the code for AWS Lambda functions that process the data received from the sensors.

## Sensors Folder

This folder contains the code for setting up and interacting with the sensors connected to the Raspberry Pi Pico W.
- SCD41: A sensor from Pimoroni for measuring CO2, temperature, and humidity.
- BME688: A sensor from Pimoroni for measuring temperature, humidity, pressure, and gas resistance.
