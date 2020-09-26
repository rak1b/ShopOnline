import socket

c = socket.socket()

ip = socket.gethostname()
port = 9010
c.connect((ip,port))
con = True

while con:
	recieved_msg =c.recv(1024).decode()
	if (recieved_msg == 'quit'):
		con = False
		c.close()
	else:
		print(recieved_msg)
		msg = input("Enter Text--")
		send_msg = c.send(msg.encode('utf-8'))



