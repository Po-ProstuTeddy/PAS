import socket 
 
HOST = '127.0.0.1'
PORT = 2900
BUFF = 1
server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.settimeout(5) 
sock.connect(server_address)
msg = "%s] UDP Calc Server is waiting for incoming connections ..."
msg = str(hex(len(msg))).ljust(20) + msg
print(msg)
try:
    sock.sendto(msg.encode(), server_address)
except socket.error as exc: 
        print("Wyjatek socket.error : {}".format(exc))

try:
    answer, server = sock.recvfrom(BUFF)
except socket.error as exc: 
    print("Wyjatek socket.error : {}".format(exc))        
print("Answer: {}".format(answer.decode()))

sock.close() 