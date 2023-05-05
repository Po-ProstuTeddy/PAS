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
PROTOCOL = 'tcp'

if check_ip(HOST):
    HOST=socket.gethostbyname(HOST)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)
try:
    result = sock.connect_ex((HOST, PORT))
    if result == 0:
        print("Port {} is *** OPEN *** on host: {}\nService: {}".format(PORT, HOST, socket.getservbyport(PORT, PROTOCOL)))
except socket.error as e:
    print (e)
        
sock.close()   
