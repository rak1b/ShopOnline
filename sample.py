import re
filename = input("Enter filename:") 
openfile = open(filename)

mylist = []
mylst = []
count = 0
for line in openfile:
	result = re.findall(r"\d+",line)
	if result:
		for i in result:
			mylist.append(i)

for i in range(len(mylist)):
	mylst.append(int(mylist[i]))
	count = count + 1

print(f"There are {count} values with a sum={sum(mylst)}")
