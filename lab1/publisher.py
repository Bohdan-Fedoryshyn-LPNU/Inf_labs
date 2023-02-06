import time

import paho.mqtt.client as mqtt
import json

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)
i=0

while True:
        i=i+1
        number = json.dumps({"number":i})
        client.publish("fedoryshyn/topic",number)
        print(number)
        time.sleep(1)
