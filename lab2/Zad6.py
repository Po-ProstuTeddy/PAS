import socket 
 
HOST = '127.0.0.1'
PORT = 2902
server_address = (HOST, PORT)

 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.settimeout(5) 
formula = ['data1', 'operator', 'data2']
buff = 4096 
sock.connect(server_address)

for f in formula:
    msg = input("Send {}: ".format(f))
    try:
        sock.sendto(msg.encode(), server_address)
    except socket.error as exc: 
        print("Wyjatek socket.error : {}".format(exc))

try:
    answer, server = sock.recvfrom(buff)
except socket.error as exc: 
    print("Wyjatek socket.error : {}".format(exc))        
print("Answer: {}".format(answer.decode())) 

sock.close() 