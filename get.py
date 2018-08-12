#import requests library
import requests
import json

#specify URL
url = 'https://jsonplaceholder.typicode.com/todos/1'

#Call REST API
response = requests.get(url)

#Print raw string
#print(response.text)

#Turn raw string into Json object
responseJson = json.loads(response.text)

#Print JSON object w/ pretty print
print(json.dumps(responseJson, indent=2))

#Print specified field within JSON
print('title: ', responseJson['title'])