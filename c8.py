FileName = input("Enter File Name : ")
OpenFile = open(FileName)

L = []
for i in OpenFile:
	L.append(i.split())
	

# MList = L[0] + L[1] + L[2] + L[3]
MList = [];
for i in range(len(L)):
	MList = MList + L[i]


RkList = []
for i in MList:
	if i not in RkList:
		RkList.append(i)
RkList.sort()
print(RkList)
