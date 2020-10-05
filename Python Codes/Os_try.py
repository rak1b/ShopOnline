import os
import re
import shutil


os.chdir("D://OSPRAC")
# Videos = ['.mkv']
# Compressed= ['.zip']
# Subtitle = ['.srt']

# types = [Videos,Compressed,Subtitle]
# print(types[1])

file_types = {
	'Videos' : '.mkv',
	'Compressed':'.zip',
	'Subtitle' : '.srt'
}

	# print()

for ex in os.listdir():
	find = re.compile(r"(\.[a-z]{3}$)")
	result = find.finditer(ex)
	for i in result:
		for key in file_types:
			if i.group(1) in file_types[key]:
				print(file_types[key])
			else:
				print("Not Found")
# 		
