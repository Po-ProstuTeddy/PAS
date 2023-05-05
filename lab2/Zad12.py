import socket 
 
HOST = '127.0.0.1'
PORT = 2908
buff = 1024 
MAX_PACKET_LENGTH = 20

def recvall(sock, msgLen):
    msg = "".encode()
    bytesRcvd = 0

    while bytesRcvd < msgLen:

        chunk = sock.recv(msgLen - bytesRcvd)

        if not chunk:
            break

        bytesRcvd += len(chunk)
        msg += chunk

    return msg

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.settimeout(2) 
server_address = (HOST, PORT)
msg = 'Hello' 
client.connect(server_address)
try:
    client.send('{:<20}'.format(msg).encode()) 
except socket.error as exc: 
    print("Wyjatek socket.error : {}".format(exc))

try:
    answer = recvall(client, MAX_PACKET_LENGTH)
    print("Answer: "+ answer.decode()) 

except socket.error as exc: 
    print("Wyjatek socket.error : {}".format(exc))

client.close() 