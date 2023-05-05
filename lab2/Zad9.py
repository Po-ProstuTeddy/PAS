import socket 
 
HOST = '127.0.0.1'
PORT = 2906
buff = 4096 
server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.settimeout(5) 
sock.connect(server_address)

try:
    sock.sendto("HOST".encode(), server_address)
except socket.error as exc: 
        print("Wyjatek socket.error : {}".format(exc))

try:
    answer, server = sock.recvfrom(buff)
except socket.error as exc: 
    print("Wyjatek socket.error : {}".format(exc))        
print("Answer: {}".format(answer.decode())) 

sock.close() 
