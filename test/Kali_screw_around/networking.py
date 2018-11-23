import socket
s = socket.socket()

ip = input('What ip do you want?: ')
port = int(input('what port do you want?: '))
print(type(ip))
print(type(port))

s.connect((ip, port))

answer = s.recv(1024)
print(answer)

s.close
