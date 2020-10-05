import re

file = open("count.txt")
for i in file:
	# print(i)
	# data = re.compile(r"\S+@\S+")
	# data = re.compile(r"\d+:\d+:\d+")
	data = re.compile(r"X-\S+-")
	result = data.finditer(i)
	for r in result:
		print(r)