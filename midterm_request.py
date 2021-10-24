#                                      Request program to obtain the html 

# import packages
import urllib.request
import os 

# Create file path 
if not os.path.exists("html_file"): 
	os.mkdir("html_file") 

# Request html
f = open("html_file/GitHub_Users.html","wb",) #opening a connection to the new file testing.html in the html_files folder
response = urllib.request.urlopen("http://45.79.253.243/index.html") #puts the request for the url in a variable to get another page (.com/?page=2)
html = response.read() #allows the html to be in a variable 
f.write(html) #write the html to the file that we opened 
f.close() #close the connection to the file 




