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


data = {"Temperature": 12, "Humidity": 20}

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

client.publish("my/test/topic", str(data))

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()




