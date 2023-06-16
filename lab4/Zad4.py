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
        data1, client_address = server_socket.recvfrom(BUFF)
        print("[{}] Client {} sent [{}]...".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),client_address,data1.decode()))

        op, client_address = server_socket.recvfrom(BUFF)
        print("[{}] Client {} sent [{}]...".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),client_address,op.decode()))

        data2, client_address = server_socket.recvfrom(BUFF)
        print("[{}] Client {} sent [{}]...".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),client_address,data2.decode()))


        if data1 and data2 and op:

            op = op.decode()

            try :

                if op == '+':
                    sent = server_socket.sendto(format(float(data1) + float(data2)).encode(), client_address)
                elif op == '-':
                    sent = server_socket.sendto(format(float(data1) - float(data2)).encode(), client_address)
                elif op == '*':
                    sent = server_socket.sendto(format(float(data1) * float(data2)).encode(), client_address)
                elif op == '/':
                    sent = server_socket.sendto(format(float(data1) / float(data2)).encode(), client_address)
                else:
                    sent = server_socket.sendto("Bad operator. I support only +, -, *, / math operators".encode(), client_address)

            except ValueError as exc:
                sent = server_socket.sendto(format(exc).encode(), client_address)

            except:
                sent = server_socket.sendto("Error".encode(), client_address)
finally:
    server_socket.close()