import json
import ssl
import time
import ubinascii
import machine

from mqtt_client import MQTTClient
import breakout_scd41
from pimoroni_i2c import PimoroniI2C
import connections
import constants

PINS_PICO_SENSOR = {"sda": 4, "scl": 5}

i2c = PimoroniI2C(**PINS_PICO_SENSOR)

breakout_scd41.init(i2c)
breakout_scd41.start()
led = machine.Pin('LED', machine.Pin.OUT)

def read_pem(file):
    with open(file, "r") as input:
        text = input.read().strip()
        split_text = text.split("\n")
        base64_text = "".join(split_text[1:-1])
        return ubinascii.a2b_base64(base64_text)
    
def publish_sensor_values():
    while True:
        co2, temperature, humidity = breakout_scd41.measure()
        led.value(True)
        payload = {
            "sensor_id": "scd41",
            "created_at": round(time.time() * 1000),
            "temperature": '{:0.2f}'.format(temperature),
            "humidity": '{:0.2f}'.format(humidity),
            "co2": '{:0.2f}'.format(co2),            
            "topic": 'SCD41'
        }
        mqtt_client.publish('SCD41', json.dumps(payload))
        print("Published")
        time.sleep(2)
        led.value(False)
        time.sleep(8)

key = read_pem(constants.MQTT_CLIENT_KEY)
cert = read_pem(constants.MQTT_CLIENT_CERT)
ca = read_pem(constants.MQTT_BROKER_CA)

mqtt_client = MQTTClient(
    constants.MQTT_CLIENT_ID,
    constants.MQTT_BROKER,
    keepalive=60,
    ssl=True,
    ssl_params={
        "key": key,
        "cert": cert,
        "server_hostname": constants.MQTT_BROKER,
        "cert_reqs": ssl.CERT_REQUIRED,
        "cadata": ca,
    },
)


led.value(True)
print(f"Connecting WLAN")
connections.connect_wlan()
print(f"Done Connecting")
led.value(False)

led.value(True)
print(f"Connecting to MQTT broker")
mqtt_client.connect()
print("Done Connecting, sending Values")
led.value(False)

print("Start publishing sensor values")
publish_sensor_values()

