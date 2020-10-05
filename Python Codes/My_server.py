import socket

s = socket.socket()

ip = socket.gethostname()
# ip = "192.168.1.4"
# ip = '103.146.42.84'
port = 3030
s.bind((ip,port))
s.listen(3)
print("Server Created\nWaiting for connection.....")
con = True

Rk,add = s.accept()
print(f"Connected to : {add}")
welcomeMsg = f"Welcome : {add}" 
Rk.send(welcomeMsg.encode('utf-8'))



while con:
	
	recieved_msg = Rk.recv(1024).decode()

	if recieved_msg == 'quit':
		con = False
		Rk.close()
	else:
		print(recieved_msg)
		sendmsg = input("Send to cilent \n -->")
		Rk.send(sendmsg.encode('utf-8'))	
			
			
