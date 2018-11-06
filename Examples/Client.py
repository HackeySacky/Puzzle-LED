import socket

host = '' # IP-Address of host
port = 5560 # Same Port as Host

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while True:
    command = input('Enter Command: ')
    if command == 'EXIT' or command == 'KILL':
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('utf-8'))

s.close()
