import socket

HOST = '127.0.0.1'  # localchost
PORT = 5005    # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
    udp_socket.connect((HOST, PORT)) # conect
    udp_socket.sendall(b'Hello, world')  # send all data
    data = udp_socket.recv(1024)

print("Recevied", repr(data))