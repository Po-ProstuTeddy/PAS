import socket
import sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2900
BUFF = 4096 
server_address = (HOST, PORT)

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
print("Starting up on {} port {}".format(HOST,PORT))
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

while True:

    #Connect client
    sock, client_address = server_socket.accept()

    try:
        print("[{}] Client {} conected...".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),client_address))

        while True:
            try:
                data = sock.recv(BUFF)

                if data: 
                    print("[{}] Client {} sent [{}]...".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),client_address,data.decode()))
                    print("[{}] Sending to client [{}]".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),strftime("%Y-%m-%d %H:%M:%S", gmtime())))
                    sock.send((strftime("%Y-%m-%d %H:%M:%S", gmtime())).encode())
                else:
                    print("[{}] Client {} is disconnected...".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),client_address))
                    break
            except socket.error as exc:
                print("[{}] Wyjatek socket.error : {}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),exc))   
            
    finally:
        sock.close()

