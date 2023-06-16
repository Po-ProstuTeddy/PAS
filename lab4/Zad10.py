import socket
import sys
from time import gmtime, strftime

def check_msg_syntax(txt):
    s = len(txt.split(";"))
    if s != 7:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad13odp" and tmp[1] == "src" and tmp[3] == "dst" and tmp[5] == "data":
            try:
                src_port = int(tmp[2])
                dst_port = int(tmp[4])
                data = tmp[6]
            except :
                return "BAD_SYNTAX:"
            if src_port == 2900 and dst_port == 35211 and data == "hello :)":
                return "TAK"
            else:
                return "NIE"
        else:
            return "BAD_SYNTAX"

HOST = '127.0.0.1'
PORT = 2909
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
            answer = check_msg_syntax(data.decode())
            print("[{}] Client {} sent [{}]...".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),client_address,data.decode()))
            server_socket.sendto(answer.encode(), client_address)
            print("[{}] Sending back to client [{}]".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),answer))
finally:
    server_socket.close()