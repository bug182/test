import socket
s = socket.socket()

ip = input(str('What ip do you want?: '))

s.connect((ip, 22))

answer = s.recv(1024)
print(answer)

s.close
