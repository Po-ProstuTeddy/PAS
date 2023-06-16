import socket, time
 
HOST = '127.0.0.1'
TCP_PORT = 2913
UDP_PORTS =[]
BUFF = 100 
TCP_server_address = (HOST, TCP_PORT)

UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
UDP_sock.settimeout(0.001) 
msg = "PING"
for x in range(0,65):
    UDP_PORT =x*1000+666
    for udp in UDP_PORTS:
            if UDP_PORT == udp:
                UDP_PORT= UDP_PORT + 1
    UDP_SERVER_ADDRESS = (HOST,UDP_PORT)
    try:
        connect = UDP_sock.connect(UDP_SERVER_ADDRESS)
        UDP_sock.sendto(msg.encode(), UDP_SERVER_ADDRESS)
        answer, server = UDP_sock.recvfrom(BUFF)
        if answer.decode() == "PONG":
            UDP_PORTS.append(UDP_PORT)
    except socket.error as exc: 
            continue

UDP_sock.close()

TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
TCP_sock.settimeout(1) 
try:
    TCP_sock.connect(TCP_server_address)
    TCP_sock.send("Hello".encode())
    answer = TCP_sock.recv(BUFF)
    print("Answer: {}".format(answer.decode()))
except socket.error as exc:
     print("Wyjatek socket.error : {}".format(exc))

TCP_sock.close()

