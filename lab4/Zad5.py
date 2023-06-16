import socket
import sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2900
BUFF = 4096 
server_address = (HOST, PORT)

# Create a UDP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
print("Starting up on {} port {}".format(HOST,PORT))
server_socket.bind(server_address)


try:
    while True:

        data, client_address = server_socket.recvfrom(BUFF)

        if data: 
            print("[{}] Client {} sent [{}]...".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),client_address,data.decode()))
            hostname = socket.gethostbyaddr(data.decode())[0]
            sent = server_socket.sendto(hostname.encode(), client_address)
            print("[{}] Sending back to client [{}]".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),hostname))
finally:
    server_socket.close()

