import urllib.request,urllib.parse,urllib.error
rk = urllib.request.urlopen("https://www.facebook.com")
for line in rk:
	print(line.decode().strip())