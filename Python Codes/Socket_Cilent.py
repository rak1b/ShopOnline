import socket

c = socket.socket()

c.connect(("localhost",9898))

print(c.recv(100).decode())

while True:
	msg = input("Type Here->")
	c.send(bytes(msg,'utf-8'))
	# if c.recv(1024):
	# 	print(c.recv(1024).decode())
	# 	ms = input("Type here->")
	# 	c.send(bytes(ms,'utf-8'))

	if msg == 'bye':
		break