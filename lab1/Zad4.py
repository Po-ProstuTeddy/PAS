import socket 

src = input("IP to hostname: ") 
print(socket.gethostbyaddr(src)) 
