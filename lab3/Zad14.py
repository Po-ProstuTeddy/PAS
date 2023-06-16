import socket 
 
HOST = '127.0.0.1'
PORT = 2909
BUFF = 4096 
server_address = (HOST, PORT)

data = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29".split()

X = int("".join(data[:2]),16)
Y = int("".join(data[2:4]),16)
Z = "".join([chr(int(x,16)) for x in data[32:]])

# print(X)
# print(Y)
# print(Z)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.settimeout(5) 
sock.connect(server_address)
msg =f"zad13odp;src;{X};dst;{Y};data;{Z}"
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