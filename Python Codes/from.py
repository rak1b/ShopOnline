FileName = input("Enter File Name :")
OpenFile = open(FileName)
count = 0

for line in OpenFile:
	if line.startswith("From"):
		f = line.split()
		if len(f) < 7:
			continue
		print(f[1])
		count = count +1
print("There were", count, "lines in the file with From as the first word")

