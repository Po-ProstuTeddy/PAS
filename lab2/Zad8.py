import socket
import sys

def check_ip(txt):
    x = txt.split(".") 
    if x.count(x) == 4: 
        for i in x: 
            if(int(i)<0 or int(i)>255): 
                return False
    return True

def check_port(host, port, protocol, timeout_in_seconds):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            try:
                service = socket.getservbyport(port, protocol)
            except socket.error as e:
                service = e
            print("Port {} is *** OPEN *** on host: {}\nService: {}\n".format(port, host, service))
    except socket.error as e:
        print (e)
    sock.close()   


HOST = sys.argv[1]
PROTOCOL = 'tcp'

if check_ip(HOST):
    HOST=socket.gethostbyname(HOST)

for i in range(1,9999):
    check_port(HOST,i,PROTOCOL,2)

        
