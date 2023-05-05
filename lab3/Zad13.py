import socket 
 
HOST = '127.0.0.1'
PORT = 2907
buff = 4096 
server_address = (HOST, PORT)

data = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"

answer = [
     ['SourcePort', 0]
     ['DestinationPort',0]
     ['Length',0]
     ['CheckSum',0]
]
for i in answer:
    b16 = ''
    b16, data = data.split(' ',1)
    x, data = data.split(' ',1)
    b16 += x
    i= int(b16, 16)
    
for i in answer:
    print(i.second())


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.settimeout(5) 
sock.connect(server_address)

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
