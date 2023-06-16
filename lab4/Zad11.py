import socket
import sys
from time import gmtime, strftime

def check_msgA_syntax(txt):
    s = len(txt.split(";"))
    if s != 9:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad15odpA" and tmp[1] == "ver" and tmp[3] == "srcip" and tmp[5] == "dstip" and tmp[7] == "type":
            try:
                ver = int(tmp[2])
                srcip = tmp[4]
                dstip = tmp[6]
                type = int(tmp[8])
                if ver == 4 and type == 6 and srcip == "212.182.24.27" and dstip == "192.168.0.2":
                    return "TAK"
                else:
                    return "NIE"
            except:
                return "NIE"
        else:
            return "BAD_SYNTAX"

def check_msgB_syntax(txt):
    s = len(txt.split(";"))
    if s != 7:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad15odpB" and tmp[1] == "srcport" and tmp[3] == "dstport" and tmp[5] == "data":

            try:
                srcport = int(tmp[2])
                dstport = int(tmp[4])
                data = tmp[6]

                if srcport == 2900 and dstport == 47526 and data == "network programming is fun":
                    return "TAK"
                else:
                    return "NIE"
            except:
                return "NIE"
        else:
            return "BAD_SYNTAX"
        
HOST = '127.0.0.1'
PORT = 2911
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
            answer = check_msgA_syntax(data.decode())
            print("[{}] Client {} sent [{}]...".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),client_address,data.decode()))
            server_socket.sendto(answer.encode(), client_address)
            print("[{}] Sending back to client [{}]".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),answer))
            if answer == "TAK":
                data, client_address = server_socket.recvfrom(BUFF)
                if data: 
                    answer = check_msgB_syntax(data.decode())
                    print("[{}] Client {} sent [{}]...".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),client_address,data.decode()))
                    server_socket.sendto(answer.encode(), client_address)
                    print("[{}] Sending back to client [{}]".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),answer))
finally:
    server_socket.close()