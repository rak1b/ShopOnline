import urllib.request, urllib.parse
import json



loc = input('Enter location: ')
serviceurl = 'http://py4e-data.dr-chuck.net/json?key=42&'


url = serviceurl + urllib.parse.urlencode({'address': loc}) #Covert mapping object to a percent-encoded ASCII text string.
print('Retrieving', url)

connection = urllib.request.urlopen(url)
data = connection.read().decode() #string from utf-8 to unicode
print('Retrieved:', len(data), 'characters')
js = json.loads(data) #deserialize 'data' to a Python object

placeid = js['results'][0]['place_id']
print('Place id', placeid)