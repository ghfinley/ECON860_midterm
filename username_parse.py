#                            Parse the Git Hub Username html File

# Import Packages 
from bs4 import BeautifulSoup
import pandas
import os

# Create File Path
if not os.path.exists("parsed_files"): #check if the file path does not exist
	os.mkdir("parsed_files") #makes a folder named parsed_files

# Create Data Frame 
df = pandas.DataFrame()

# Place the html in the soup 
file_name = "html_file/GitHub_Users20211025215450.html" 
f = open(file_name,"r")
soup = BeautifulSoup(f.read(),"html.parser")
f.close()

#print(soup)

divs = soup.find("div", {"class": "grid grid-cols-3 gap-4"})
names = divs.find_all("div")
#print(names)

for name in names:
	github_id = name.get("ghid")
	#print(github_id)
	df = df.append({
	 	'userid' : github_id,
	 	}, ignore_index = True
	 	)
	df = df.drop_duplicates()

df.to_csv("parsed_files/github_id.csv")
