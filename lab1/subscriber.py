import paho.mqtt.client as mqtt
from time import sleep


broker="test.mosquitto.org"
port=1883

def on_message(client, userdata, message):
    print("Received message: " + str(message.payload))

topic=("fedoryshyn/topic",2)
client1= mqtt.Client()
client1.connect(broker,port)
client1.subscribe(topic)
print("Subscribing to topics ",topic)
sleep(2)
client1.loop_start()
client1.on_message = on_message
