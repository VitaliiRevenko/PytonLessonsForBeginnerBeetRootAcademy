import socket

import argparse
parser = argparse.ArgumentParser(description="Server UDP")
parser.add_argument('--host', '-i', default='127.0.0.1', required=False, help='Which IP adress')
parser.add_argument('--port', '-p', default='5000', type=int, required=False, help='Which port')
parser.add_argument('--buffer_size', '-b', default='1024', type=int, required=False, help='Buffer size')
args = parser.parse_args()
print(args)

localIP = "127.0.0.1"
localPort = 5000
bufferSize = 1024

msgFromServer = "Hi UDP Client"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# Listen for incoming datagrams

while (True):
    data = UDPServerSocket.recvfrom(bufferSize) # read data from socket
    message = data[0]
    address = data[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)