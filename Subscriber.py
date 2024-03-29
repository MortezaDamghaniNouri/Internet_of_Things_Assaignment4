import paho.mqtt.client as paho
# This library is used for making directories in Windows
import os

output_file = open("E:\MyCodes\Web Codes\IoT_HW4_MQTT_Subscriber\Home_Content.txt", "wt")
output_file.write("\n")
output_file.close()

output_file = open("E:\MyCodes\Web Codes\IoT_HW4_MQTT_Subscriber\Farm_Content.txt", "wt")
output_file.write("\n")
output_file.close()


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))


def on_message(client, userdata, msg):
    received_payload = str(msg.payload)
    received_payload = received_payload.rstrip("\"")
    received_payload = received_payload.lstrip("b\"")
    print("Received payload: " + received_payload)
    if received_payload.find("Home") != -1:
        output_file = open("E:\MyCodes\Web Codes\IoT_HW4_MQTT_Subscriber\Home_Content.txt", "at")
        output_file.write(received_payload + "\n")
        output_file.close()
    if received_payload.find("Farm") != -1:
        output_file = open("E:\MyCodes\Web Codes\IoT_HW4_MQTT_Subscriber\Farm_Content.txt", "at")
        output_file.write(received_payload + "\n")
        output_file.close()







client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
# enable TLS
client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("Morteza", "Morteza9625801")

# connect to HiveMQ Cloud on port 8883
client.connect("a014b958335a4ba195e2715edf3ee571.s2.eu.hivemq.cloud", 8883)

# subscribe to the topic "my/test/topic"
client.subscribe("my/test/topic", qos=1)

client.loop_forever()





