# iot_core

Raspberry Pi Pico W - sensors setup for sending data through MQTT protocol to AWS IoT Core

## Lambda Folder

This folder contains the code for AWS Lambda functions that process the data received from the sensors.

## Web_app folder

This folder contains contains code for a web application that is used for visualizing sensor data. This web app is designed to display the data from csv file collected from the sensors connected to the Raspberry Pi Pico W. It provides a user-friendly interface for viewing and analyzing the sensor readings, allowing users to easily interpret and visualize the data in a meaningful way.

## Sensors Folder

This folder contains the code for setting up and interacting with the sensors connected to the Raspberry Pi Pico W.
- SCD41: A sensor from Pimoroni for measuring CO2, temperature, and humidity.
- BME688: A sensor from Pimoroni for measuring temperature, humidity, pressure, and gas resistance.
