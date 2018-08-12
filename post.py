#import requests library for url requests
import requests
#import json library for json load and parsing
import json

#specify URL
url = 'https://jsonplaceholder.typicode.com/posts'

#When using POST, you need to specify the Content-Type header as application/json
headers = {'content-type': 'application/json'}

#When using POST, you need to specify the body
payload = {
    "userId": 11,
    "id": 101,
    "title": "carpe diem",
    "body": "et tu brute?"
  }

#Note: jsonplaceholder URL doesn't action post, but simulates return as if it did
postEntry = requests.post(url, data=json.dumps(payload), headers=headers)


###Following code would check results after post, but jsonplaceholder
# simulates post, but doesn't actually create it on the server...
# if a real server was stood up, the
# following would work to see the
# results of the post

#Call REST API
response = requests.get(url)

#Print raw string
#print(response.text)

#Turn raw string into Json object
#responseJson = json.loads(response.text)

#Another way to turn raw string into Json object
responseJson = response.json()

#Print entire JSON object as a string w/ pretty print
#print(json.dumps(responseJson, indent=2))

#for each entry returned, print title

for responseJson in responseJson:
    if responseJson['id'] == 101:
        print('userid:', responseJson['id'])
        print('id:', responseJson['id'])
        print('title:', responseJson['title'])
        print('body:', responseJson['id'])