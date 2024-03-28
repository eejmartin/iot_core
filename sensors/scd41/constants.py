import ubinascii
import machine

SSID = ""  # Network name
PASSWORD = ""  # WiFi password

MQTT_CLIENT_ID = ubinascii.hexlify(machine.unique_id())
MQTT_CLIENT_KEY = "*****-private.pem.key"
MQTT_CLIENT_CERT = "*****-certificate.pem.crt"
MQTT_BROKER = ""
MQTT_BROKER_CA = "AmazonRootCA1.pem"

"""
This module contains constants used for IoT sensor communication.

- SSID: The network name for the WiFi connection.
- PASSWORD: The password for the WiFi connection.
- MQTT_CLIENT_ID: The unique ID for the MQTT client.
- MQTT_CLIENT_KEY: The private key file for the MQTT client.
- MQTT_CLIENT_CERT: The certificate file for the MQTT client.
- MQTT_BROKER: The address of the MQTT broker.
- MQTT_BROKER_CA: The CA certificate file for the MQTT broker.
"""
