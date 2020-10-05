import os
import re
import shutil

def vidfile(x):
	shutil.move(x,f'Video Files/{x}')
	print("Successfully moved ")

def zipfile(x):
	shutil.move(x,f'zip Files/{x}')
	print("Successfully moved ")

def subfile(x):
	shutil.move(x,f'Subs/{x}')
	print("Successfully moved ")


os.chdir("D://OSPRAC")
videos = ['.mkv']
zipf = ['.zip']
sub = ['.srt']
for ex in os.listdir():
	# print(ex)
	find = re.compile(r"(\.[a-z]{3}$)")
	result = find.finditer(ex)
	for i in result:
		# print(i.group(1))
		if i.group(1) in videos:
			# filename = str(ex)
			vidfile(ex)
		if i.group(1) in zipf:
			zipfile(ex)

		if i.group(1) in sub:
			subfile(ex)
			


