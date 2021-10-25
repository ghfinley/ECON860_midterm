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
file_name = "html_files/GitHub_Users20211025010847.html"
f = open(file_name,"r")
soup = BeautifulSoup(f.read(),"html.parser")
f.close()

body = soup.find("body")
divs = body.find_all("div",{"class":"userid"})

div = divs[0]

for div in divs:
	 user_id = body.find("div",{"class":"userid"})["ghid"] # ** this prints the first username 
	 print(user_id)
	 df = df.append({
	 	'userid' : user_id,
	 	}, ignore_index = True
	 	)

df.to_csv("parsed_files/githubid.csv")

# span = soup.find("span")
# all_divs = span.find_all("div")
# #print(all_divs)
# # print(all_divs[0].find("div",{"class":"userid"})["ghid"])
# # print(all_divs[1].find("div",{"class":"userid"})["ghid"])
# # print(all_divs[2].find("div",{"class":"userid"})["ghid"])
# # print(all_divs[3].find("div",{"class":"userid"})["ghid"])


# divs_wanted = all_divs[4:734]
# #print(divs_wanted)
# divs_wanted_1 = all_divs[4]
# #print(divs_wanted_1)
# #all_divs[4].find["ghid"]

# divs_wanted2 = all_divs[1]
# #print(divs_wanted2)
# print(divs_wanted2.find_all("div","class":"userid"))


#divs = span.find_all("div",{"class":"userid"})
#print(divs)
#print[divs[1]]
# x = div = divs[0]	
# y = span.find("div",{"class":"userid"})["ghid"]
# print(x)
# print(y)
#divs[0].find("div",{"class":"userid"})["ghid"]
#print(divs[0])
# for  div in divs:

# 	print(span.find("div",{"class":"userid"})["ghid"]) # ** this prints the first username 

#print(span.find("div",{"class":"userid"})["ghid"]) # ** this prints the first username 

#divs = soup.find_all("div")
#divs_wanted = divs.find("div",{"class":"userid"})

#print(span.find("div",{"class":"userid"})["ghid"])







#python3 username_parse.py 