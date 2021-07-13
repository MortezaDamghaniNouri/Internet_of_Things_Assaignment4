import socket

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

serverAddressPort = ("192.168.1.101", 20001)

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
msgFromClient = "put"

bytesToSend = str.encode(msgFromClient)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromClient = "10"

bytesToSend = str.encode(msgFromClient)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)



msgFromClient = "farm"

bytesToSend = str.encode(msgFromClient)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)






i = 0
while i < 10:
    msgFromClient = str(data[i])
    bytesToSend = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    i += 1



msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)