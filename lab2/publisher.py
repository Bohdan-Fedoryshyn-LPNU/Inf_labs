import json
import random
import time

import paho.mqtt.client as mqtt
from time import sleep

broker="demo.thingsboard.io"
port=1883
username = "0rXKeLbdlOGriHBp3ynM"
password = ""
def on_message(client, userdata, message):
    print("Received message: " + str(message.payload))
topic="iotlab/devices/telemetry"

client= mqtt.Client()
client.username_pw_set(username,password)
client.connect(broker,port)

data = {}

for i in range(100):
    data["data1"] = random.uniform(1,100)
    data["data2"] = random.uniform(1,100)
    data["data3"] = random.uniform(1,100)
    data["data4"] = random.uniform(1,100)

    data_out = json.dumps(data)
    print("Topic:  ",topic, " Data: ", data_out )
    ret = client.publish(topic,data_out,2)
    time.sleep(1)
    client.loop()

client.disconnect()


