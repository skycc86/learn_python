import sys,os,socket

host='localhost'
port=8080
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s=socket.socket()
s.bind((host,port))

s.listen(1)
print('server is listening ...')
c,addr=s.accept()
print("connection from " + str(addr))
c.send("Hello i am server".encode())
while True:
  data=c.recv(1024)
  if not data:
    break
  print("receive " + data)
  data=data.upper()
  c.send(data)
  print("sending " + data)
s.close()