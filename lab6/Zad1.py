import smtplib, telnetlib
from email.mime.base import MIMEBase

HOST = 'smtp.interia.pl'
PORT = 587
CONN_CLOSED = b"Connection closed by foreign host."

nadawca = "pas2017@interia.pl"
nadawca_haslo = "P4SInf2017"
odbiorca = "kylomm@gmail.com"
temat = "Temat"
tresc= "Treść"

try:
    client = telnetlib.Telnet(HOST,PORT)
    print(client)
    msg = client.read_some()
    print(f'{msg.decode()}')

    client.write("HELO kasiula".encode('ascii') + b"\n")
    msg = client.read_until(CONN_CLOSED,1)
    print(f'{msg.decode()}') 
    auth = "AUTH LOGIN\n" + "334 VXNlcm5hbWU6\n" + "cGFzMjAxN0BpbnRlcmlhLnBs\n" + "334 UGFzc3dvcmQ6\n" + "UDRTSW5mMjAxNw==\n"
    client.write(auth.encode())
    msg = client.read_until(CONN_CLOSED,1)
    print(f'{msg.decode()}') 

    # client.write("EHLO kasiula".encode('ascii') + b"\n")
    # msg = client.read_until(CONN_CLOSED,1)
    # print(f'{msg.decode()}') 
    # server = smtplib.SMTP(serwer, port)
    # print(server)
    # x = server.starttls()
    # print(x)
    # x = server.ehlo("kasiula")
    # print(x)
    # x = server.login(MIMEBase(nadawca),MIMEBase(nadawca_haslo))
    # print(x)
    # message = f'temat: {temat}\n\n{tresc}'

    # x = server.sendmail(nadawca, odbiorca, message)
    # print(x)
    # print(f'wyslano wiadomosc od {nadawca} do {odbiorca}')
except Exception as e:
    print(f'{e}')
finally:
    client.close()