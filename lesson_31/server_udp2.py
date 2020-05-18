import socket

import argparse

if __name__ == '__main__':

    def load_conf():    # Function for load server configuration
        parser = argparse.ArgumentParser(description="Server UDP")
        parser.add_argument('--host', '-i', default='127.0.0.1', required=False, help='Which IP adress')
        parser.add_argument('--port', '-p', default='5000', type=int, required=False, help='Which port')
        parser.add_argument('--buffer_size', '-b', default='1024', type=int, required=False, help='Buffer size')
        args = parser.parse_args()
        print(args)
        localIP = "127.0.0.1"
        localPort = 5000
        global bufferSize
        bufferSize = 1024

        msgFromServer = "Hi UDP Client"
        global bytesToSend
        bytesToSend = str.encode(msgFromServer)

        # Create a datagram socket
        global UDPServerSocket
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # Bind to address and ip
        UDPServerSocket.bind((localIP, localPort))
        print("UDP server up and listening")

    def start_server(): # Function for start server
        data = UDPServerSocket.recvfrom(bufferSize)  # read data from socket
        message = data[0]
        address = data[1]
        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)
        print(clientMsg)
        print(clientIP)

        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)

    load_conf()
    try:
        # Listen for incoming datagrams
        while (True):
            start_server()
    except:
        raise ConnectionError