import re
ls = [".mkv","mp4"]
sub =[".srt",".ass"]

filename = open('files.txt')
for i in filename:
	pattern = re.compile(r"(\.[a-z]{3}$)")
	search = pattern.finditer(i)
	# print(i)
	for ext in search:
		# print(f"\n \n filename__{i}____and ___{ext}___")
		# print(ext.group(1))
		if ext.group(1) in ls:
			print(f"{i} goes to Movies")
		else:
			print(f"{i} goes to Sub")


