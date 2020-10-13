myfile = input("Enter File name:")
opFile = open(myfile)

for i in opFile:
	print((i.rstrip()).upper())