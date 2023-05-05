import socket
import sys

def check_ip(txt):
    x = txt.split(".") 
    if x.count(x) == 4: 
        for i in x: 
            if(int(i)<0 or int(i)>255): 
                return False
    return True

HOST = sys.argv[1]
PORT = int(sys.argv[2])

if check_ip(HOST):
    HOST=socket.gethostbyname(HOST)

server_address = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(server_address)
    print("Connected with {} {}".format(HOST, PORT))

except socket.error as e:
    print("Connection failed {} {}".format(HOST, PORT))

sock.close()
