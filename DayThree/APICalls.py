import requests
import json
get_url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(get_url)

print(response.status_code) #200 means success
data = response.json() #Data

param = "1"
response_with_param = requests.get(get_url,param)
data_with_param = response.json()
print(data_with_param)

with open("apicall.json", mode="w") as file:
    json.dump(data_with_param,file,indent=4)

post_url = "https://jsonplaceholder.typicode.com/posts"
data_to_post = {
    "title": "My first API",
    "body": "Learning API calls",
    "userId": 1
}
response_with_post = requests.post(post_url,data_to_post)
print(response_with_post.status_code)


#With headers
headers = {
    "Content-Type": "application/json"
}

response_with_headers = requests.get(get_url, headers=headers)
print(response_with_headers.json())
