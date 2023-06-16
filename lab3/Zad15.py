import socket 
 
HOST = '127.0.0.1'
PORT = 2911
BUFF = 4096 
server_address = (HOST, PORT)

data = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e".split()

X = int(data[0][0],16)
Y = ".".join([str(int(x, 16)) for x in data[12:16]])
Z = ".".join([str(int(x, 16)) for x in data[16:20]])
W = int(data[9],16)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.settimeout(5) 
sock.connect(server_address)
msg =f"zad15odpA;ver;{X};srcip;{Y};dstip;{Z};type;{W}"
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

if(answer.decode()=="TAK"):
    X = int("".join(data[20:22]), 16)
    Y = int("".join(data[22:24]), 16)
    Z = "".join([chr(int(x, 16)) for x in data[52:]])
    msg = f"zad15odpB;srcport;{X};dstport;{Y};data;{Z}"
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
