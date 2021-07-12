import paho.mqtt.client as paho


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

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





