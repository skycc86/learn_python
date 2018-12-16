import sys,os,socket

host='localhost'
port=8080
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s=socket.socket()
print('making connetion to server')
s.connect((host,port))
print('connection successful to server')

msg=s.recv(1024)
print('receive {}'.format(msg.decode()))
msg=raw_input('->')
while msg!='q':
  s.send(msg)
  print("sending " + msg)
  data=s.recv(1024)
  print("receive " + data)
  msg=raw_input('->')
s.close()