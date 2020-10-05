import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
# url = 'http://py4e-data.dr-chuck.net/known_by_Peige.html'

mylist = []
url = input("Enter url:")
mylist.append(url)
pos = int(input('Position:'))
process = int(input('Process:'))

def webScrap(url_link,mypos,):
	html = urllib.request.urlopen(url_link).read()
	soup = BeautifulSoup(html,'html.parser')
	count = 0
	position = mypos
	link = soup.find_all('a')
	for i in link:
		count = count + 1
		if count == mypos :
			up_link= i.get('href')
			break


	return up_link




for i in range(process):
	v = webScrap(mylist[i],pos)
	mylist.append(v)
	print(f'retrieving {v}')

