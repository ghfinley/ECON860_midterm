import json
import requests
import pandas
import os 
import time






f = open("token","r")
token = f.read()
f.close()

f = open("username","r")
username = f.read()
f.close()


github_session = requests.Session()
github_session.auth = (username,token)


access_point = "https://api.github.com"
user_url = access_point +"/users/sco"
results = json.loads(github_session.get(user_url).text)
print(results)
