import socket 
 
HOST = '127.0.0.1'
PORT = 2901
server_address = (HOST, PORT)

 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.settimeout(5) 
msg = 'Hello' 
buff = 4096 
sock.connect(server_address)
while msg != 'EXIT':
    msg = input("Send to {} on port {}: ".format(HOST, PORT))
    try:
        sock.sendto(msg.encode(), server_address)
        answer, server = sock.recvfrom(buff)
    except socket.error as exc: 
        print("Wyjatek socket.error : {}".format(exc))
    print("Answer: {}".format(answer.decode())) 

sock.close() 