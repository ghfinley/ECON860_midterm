import json
import requests
import pandas
import os 
import time

# Create Data Frame
df = pandas.DataFrame()

# Import the Parsed Username .csv file
df_usernames = pandas.read_csv("parsed_files/github_id.csv")


f = open("token","r")
token = f.read()
f.close()

f = open("username","r")
username = f.read()
f.close()


github_session = requests.Session()
github_session.auth = (username,token)


access_point = "https://api.github.com"


for userid in df_usernames['userid']:
	print(userid)
	user_url = access_point +"/users/" + userid
	results = json.loads(github_session.get(user_url).text)
	#print(results)

	user_id = results['id']
	avatar_url = results['avatar_url']
	url = results['url']
	followers = results['followers']
	following = results['following']
	public_repos = results['public_repos']
	name = results['name']
	company = results['company']
	blog = results['blog']
	location = results['location']
	hireable = results['hireable']
	bio = results['bio']
	created = results['created_at']
	last_updated = results['updated_at']


	starred_url = (results['starred_url'])
	result= json.loads(github_session.get(starred_url).text)
	stars = result

	repos_url = (results['repos_url'])
	result = json.loads(github_session.get(repos_url).text)

	#print(result)

	project_names = [item['name'] for item in result] #array with all the project names


	descriptions = [item['description'] for item in result] #array with all the descriptions

	languages = [item['language'] for item in result] #array with all the languages

	df = df.append({
		'ID' : user_id,
		'Avatar_url' : avatar_url,
		'url': url,
		'Followers' : followers,
		'Following' : following,
		'Stars' : stars,
		'Public_Repos' : public_repos,
		'Name' : name, 
		'Company' : company,
		'blog' : blog,
		'Location' : location,
		'Hireable' : hireable,
		'Bio' : bio, 
		'Created' : created,
		'Last_Updates' : last_updated,
		'Project_Names' : project_names,
		'Project_descriptions' : descriptions,
		'Project_Languages' : languages
		}, ignore_index = True
		)
	time.sleep(30)

df.to_csv("parsed_files/github_download2.csv")


	

