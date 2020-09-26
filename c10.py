filename = "count.txt"
openfile = open(filename)

mydict = {}
mylist = []
mytupp = []

for line in openfile:
	if line.startswith("From") :
		words = line.split()
		if len(words)==7:
			# print(words)
			# print(words[len(words)-2])
			dates = words[len(words)-2].split(':')
			mylist.append(dates[0])
			
for i in mylist:
	mydict[i] = mydict.get(i,0)+1

for k,v in mydict.items():
	mytupp.append((k,v))
	# print(k,v)

lst = sorted(mytupp)
print(lst)
for k,v in lst:
	print(k,v)
# print(mylist)

# for cut in words:
# 	print(words[cut])


# rk = 'From: louis@media.berkeley.edu'
# for line in rk:
# 	rkv = rk.split()
# print(len(rkv))
