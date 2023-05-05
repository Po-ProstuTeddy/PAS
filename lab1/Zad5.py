import socket 
 
src = input("hostname to IP: ") 
print(socket.gethostbyname(src))