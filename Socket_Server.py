import socket

s = socket.socket()
s.bind(('localhost',9898))
print("Server Created\nWaiting for connections........")
s.listen(4)
while True:
	c,add= s.accept() 
	print("Connected With : ",add)
	c.send(bytes("Welcome",'utf-8'))
	if c.recv(1024):
		print(c.recv(1024).decode())
		ms = input("Type here->")
		c.send(bytes(ms,'utf-8'))

	c.close()