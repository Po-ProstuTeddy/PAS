import socket, time
 
HOST = '127.0.0.1'
PORT = 2900
BUFF = 4096 
server_address = (HOST, PORT)
#TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.settimeout(5) 
msg = "Hello"
start_time = time.time()
try:
    sock.connect(server_address)
    sock.send(msg.encode())
    answer = sock.recv(BUFF)
    print("Answer: {}".format(answer.decode()))
except socket.error as exc: 
        print("Wyjatek socket.error : {}".format(exc))
sock.close()
end_time = time.time()
print("Elapsed time TCP: {}ms".format((end_time-start_time)*1000))
time.sleep(1)
#UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.settimeout(5) 
msg = "Hello"
start_time = time.time()
try:
    sock.connect(server_address)
    sock.sendto(msg.encode(),server_address)
    answer, server_address = sock.recvfrom(BUFF)
    print("Answer: {}".format(answer.decode()))
except socket.error as exc: 
        print("Wyjatek socket.error : {}".format(exc))
sock.close()
end_time = time.time()
print("Elapsed time UDP: {}ms".format((end_time-start_time)*1000))

# X w moim przypadku czas z wykozystaniem gnizda TCP był krotszy.
# X Czas powinien być krotszy przy użyciu gniazda UDP ze względu że nie wymaga on ustanowionego połączenia oraz nie retransmituje zagubionych pakietów.
# X Zaletą gniazda TCP w przeciwieństwie do UDP jest to że zapenia on dostarczenie wszystkich pakietów w zamian za wolniejsze połączenie, UDP jest szybszy można go wykozystywać do broadcast'u ale nie zapewnia dostarczenia wszystkich pakietów.