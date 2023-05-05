import socket 
 
 
sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sockIPv4.settimeout(5) 
address = (socket.gethostbyname("ntp.task.gda.pl"), 13) 
msg = 'time' 
buff = 1024 
try: 
    sockIPv4.connect(address) 
except socket.error as exc: 
    print("Wyjatek socket.error : %s" % exc) 
time = sockIPv4.recvfrom(buff)[0]
print(time.decode()) 
sockIPv4.close()