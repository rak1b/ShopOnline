import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

# url = input("Enter Url:")
url = 'http://py4e-data.dr-chuck.net/known_by_Peige.html'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

# tags = soup('body')
# for i in tags:
# 	print(i.get('div'))

para = soup.find_all('a')
for i in para:
	print(i.get('href'))
	# print(i)
# print(para)