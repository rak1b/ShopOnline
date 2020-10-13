FileName = input("Enter File Name : ")
OpenFile = open(FileName)
Count = 0
Sum = 0

for line in OpenFile:
	if line.startswith("X-DSPAM-Confidence"):
			startPos = line.find(":")
			number = line[startPos + 1:].strip()
			Count = Count + 1
			Sum = Sum + float(number)


print(f"Found {Count} times")
Avg = Sum / Count
print("Average : ",Avg)

