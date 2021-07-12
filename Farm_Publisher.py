import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))


# Main part of the code starts here


data = [
{"ID": "Farm1", "Humidity": 12, "Chemicals": "Enough", "Water Time": "False", "Temperature": 23, "Light": "Enough"},
{"ID": "Farm2", "Humidity": 10, "Chemicals": "Not Enough", "Water Time": "True", "Temperature": 50, "Light": "Not Enough"},
{"ID": "Farm3", "Humidity": 11, "Chemicals": "Enough", "Water Time": "True", "Temperature": 32, "Light": "Enough"},
{"ID": "Farm4", "Humidity": 16, "Chemicals": "Enough", "Water Time": "True", "Temperature": 67, "Light": "Enough"},
{"ID": "Farm5", "Humidity": 14, "Chemicals": "Not Enough", "Water Time": "True", "Temperature": 76, "Light": "Enough"},
{"ID": "Farm6", "Humidity": 13, "Chemicals": "Not Enough", "Water Time": "True", "Temperature": 55, "Light": "Enough"},
{"ID": "Farm7", "Humidity": 10, "Chemicals": "Enough", "Water Time": "True", "Temperature": 45, "Light": "Enough"},
{"ID": "Farm8", "Humidity": 10, "Chemicals": "Not Enough", "Water Time": "False", "Temperature": 20, "Light": "Enough"},
{"ID": "Farm9", "Humidity": 10, "Chemicals": "Enough", "Water Time": "False", "Temperature": 15, "Light": "Not Enough"},
{"ID": "Farm10", "Humidity": 19, "Chemicals": "Not Enough", "Water Time": "False", "Temperature": 12, "Light": "Not Enough"},
]

# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("Morteza", "Morteza9625801")

# connect to HiveMQ Cloud on port 8883
client.connect("a014b958335a4ba195e2715edf3ee571.s2.eu.hivemq.cloud", 8883)

# subscribe to the topic "my/test/topic"
client.subscribe("my/test/topic")

# publish "Hello" to the topic "my/test/topic"

i = 0
while i < 10:
    client.publish("my/test/topic", str(data[i]))
    i += 1

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()




