import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_943647.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

summ = 0
count = 0
span = soup.findAll('span')
for i in span:
	count = count+1
	summ = summ + int(i.getText())

print(f"Count {count} \nSum {summ}")