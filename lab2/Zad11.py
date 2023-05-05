import socket 
 
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.settimeout(5) 
HOST = '127.0.0.1'
PORT = 2908
buff = 1024 
server_address = (HOST, PORT)
msg = 'Hello'
client.connect(server_address)
try:
    client.send('{:<20}'.format(msg).encode()) 
except socket.error as exc: 
    print("Wyjatek socket.error : {}".format(exc))

try:
    answer = client.recv(buff)
    print("Answer: "+ answer.decode()) 

except socket.error as exc: 
    print("Wyjatek socket.error : {}".format(exc))

client.close() 