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
{"ID": "Home1", "Parking": "Full", "Energy Consumption(Watt)": 10, "Lights": "off", "Temperature": 23, "Doors": "Locked"},
{"ID": "Home2", "Parking": "Empty", "Energy Consumption(Watt)": 12, "Lights": "off", "Temperature": 50, "Doors": "Unlocked"},
{"ID": "Home3", "Parking": "Full", "Energy Consumption(Watt)": 1200, "Lights": "on", "Temperature": 32, "Doors": "Unlocked"},
{"ID": "Home4", "Parking": "Full", "Energy Consumption(Watt)": 2000, "Lights": "on", "Temperature": 67, "Doors": "Unlocked"},
{"ID": "Home5", "Parking": "Empty", "Energy Consumption(Watt)": 3000, "Lights": "on", "Temperature": 76, "Doors": "Unlocked"},
{"ID": "Home6", "Parking": "Empty", "Energy Consumption(Watt)": 4500, "Lights": "on", "Temperature": 55, "Doors": "Locked"},
{"ID": "Home7", "Parking": "Empty", "Energy Consumption(Watt)": 1800, "Lights": "off", "Temperature": 45, "Doors": "Locked"},
{"ID": "Home8", "Parking": "Full", "Energy Consumption(Watt)": 10000, "Lights": "on", "Temperature": 20, "Doors": "Unlocked"},
{"ID": "Home9", "Parking": "Full", "Energy Consumption(Watt)": 2220, "Lights": "off", "Temperature": 15, "Doors": "Locked"},
{"ID": "Home10", "Parking": "Empty", "Energy Consumption(Watt)": 3000, "Lights": "off", "Temperature": 12, "Doors": "Unlocked"},
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




