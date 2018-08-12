#import requests library for url requests
import requests
#import json library for json load and parsing
import json

#specify URL
url = 'https://jsonplaceholder.typicode.com/posts'

#Call REST API
response = requests.get(url)

#Print raw string
#print(response.text)

#Turn raw string into Json object
#responseJson = json.loads(response.text)

#Another way to turn raw string into Json object
responseJson = response.json()

#Print entire JSON object as a string w/ pretty print
print(json.dumps(responseJson, indent=2))

#for each entry returned, print title
'''
for responseJson in responseJson:
    if responseJson['id'] == 100:
        print('id:', responseJson['id'])
        print('title:', responseJson['title'])
'''