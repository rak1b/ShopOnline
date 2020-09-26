import os
import re
import shutil

ChngDir = input("Enter Directory:")
os.chdir(ChngDir)

file_types = {
	'Videos' : '.mkv',
	'Compressed':'.zip,.rar',
	'Subtitle' : '.srt',
	'Image' : '.png,.jpg'
}

def Move_File(filename):
	shutil.move(filename,f'{key} Files/{filename}')
	print(f"Successfully Moved to {key} Files ")


def Create_Folder(newFile):
	if not os.path.exists(f"{newFile} Files"):
		os.mkdir(f"{newFile} Files")



for ex in os.listdir():
	find = re.compile(r"(\.[a-z]{3}$)")
	result = find.finditer(ex)
	for i in result:
		for key in file_types:
			if i.group(1) in file_types[key]:
				print(f"Found in {key} List")
				Create_Folder(key)
				Move_File(ex)




