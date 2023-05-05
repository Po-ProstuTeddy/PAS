import socket 
 
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.settimeout(5) 
HOST = '127.0.0.1'
PORT = 2900
server_address = (HOST, PORT)
msg = 'Hello' 
buff = 1024 
client.connect(server_address)
while msg != 'EXIT':
    msg = input("Send to {} on port {}: ".format(HOST, PORT))
    try:
        client.send(msg.encode()) 
        answer = client.recv(buff)
    except socket.error as exc: 
        print("Wyjatek socket.error : {}".format(exc))
    print("Answer: "+ answer.decode()) 
client.close() 