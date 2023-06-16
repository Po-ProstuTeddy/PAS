import socket
import random
import sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2911
BUFF = 4096 
server_address = (HOST, PORT)

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
print("Starting up on {} port {}".format(HOST,PORT))
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
randomNumber = random.randint(0,100)
data = b'-1'
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
                    if(int(data) == randomNumber):
                        sock.send("Win!!!".encode())
                        print("[{}] Sending back to client [{}]".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),"Win"))
                        sys.exit()
                    elif(int(data) < randomNumber):
                        sock.send("Too cold..".encode())
                        print("[{}] Sending back to client [{}]".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),"Too cold.."))
                    else:
                        sock.send("Too hot..".encode())
                        print("[{}] Sending back to client [{}]".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),"Too hot.."))
                else:
                    print("[{}] Client {} is disconnected...".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),client_address))
                    break
            except socket.error as exc:
                print("[{}] Wyjatek socket.error : {}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),exc))   
            
    finally:
        sock.close()