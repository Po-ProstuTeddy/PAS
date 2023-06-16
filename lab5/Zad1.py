import socket 
 
HOST = '127.0.0.1'
PORT = 2911
BUFF = 4096 
server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.settimeout(5) 
try:
    sock.connect(server_address)
    msg = input("Send your number : ")
    sock.send(msg.encode())
    answer, server = sock.recvfrom(BUFF)
    print("Answer: {}".format(answer.decode()))
except socket.error as exc: 
        print("Wyjatek socket.error : {}".format(exc))

sock.close() 