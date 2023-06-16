import socket 
 
HOST = '127.0.0.1'
PORT = 2910
BUFF = 4096 
server_address = (HOST, PORT)

data = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e".split()

X = int("".join(data[:2]),16)
Y = int("".join(data[2:4]),16)
Z = "".join([chr(int(x,16)) for x in data[8:]])

# print(X)
# print(Y)
# print(Z)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.settimeout(5) 
sock.connect(server_address)
msg =f"zad14odp;src;{X};dst;{Y};data;{Z}"

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
