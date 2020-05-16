import socket

#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 5005)
print("starting up on {} port {}".format(*server_address))

# Listen for incoming connection
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            data = connection.recv(1024)  # read data from socket
            print('recevied{!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall()
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()