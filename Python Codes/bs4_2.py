import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url = 'http://py4e-data.dr-chuck.net/known_by_Peige.html'
process = 4
number = 3

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
count = 0
link = soup.find_all('a')
for i in link:
	print(i.get('href'))
	count = count + 1
	if count == number -1:
		# print(count)
		up_link = i.get('href')
		break
print(up_link)

for i in range(process):
	html = urllib.request.urlopen(up_link).read()
	soup = BeautifulSoup(html,'html.parser')

