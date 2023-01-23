import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)
data = response.json()[0:20]  # only first 20 records

file = open("data.json", "w")  # open new file
json.dump(data, file)   # save data to new file opened