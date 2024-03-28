import ubinascii
import machine

SSID = "" #Network name
PASSWORD = "" #WiFi password

MQTT_CLIENT_ID = ubinascii.hexlify(machine.unique_id())
MQTT_CLIENT_KEY = "*****-private.pem.key"
MQTT_CLIENT_CERT = "*****-certificate.pem.crt"
MQTT_BROKER = ""
MQTT_BROKER_CA = "AmazonRootCA1.pem"