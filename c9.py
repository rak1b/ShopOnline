# filename = input("Enter File Name :")
filename = "count.txt"
OpenFile = open(filename)
data = {}
mist = []
for line in OpenFile:
	if line.startswith("From"):
		words = line.split()
		if len(words) <7:
			mist.append(words[1])
for word in mist:		
	data[word] = data.get(word,0) + 1

print(data)

max_val = 0 
max_k = 0
for k,v in data.items():
	if v > max_val:
		max_val = v
		max_k = k
print(max_k,max_val)

# school = {
# 	's1':'Rakib',
# 	's2':'Rk',
# 	's3':'Rkb'
# }

# for i in range(5):
# 	for j in range(5):
# 		inp = input("Enter :")
# 		school[inp] = school.get(inp,j)
# 		print(school[inp])
# 		print(school)




# school = school.get("s4",12)
