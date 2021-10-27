
This repository scrapes the website: http://45.79.253.243/index.html for the GitHub usernames and uses those usernames to download data for each of the usernames via the GitHub API.

							Step 1:
Create a git repo and push to GitHub if you choose 

Run the midterm_request.py program 

							Step 2:

Run the username_parse.py program
Be sure to make sure that on line 16 that reference the location where you saved the .html file from the midterm_request.py program

							Step 3:

Create a file called token and place your distinct API token from GitHub there 
Create a username file and place your username in there
Create a .gitignore file for you to place the token and username file in there

							Step 4:

Run the github_downloader.py program 
For lines 32:49, you can searh the json and add any more or less variables that you want to parse, just make sure too add or drop from lines 69:86

** The only issue with the code is the result for the number of stars for the GitHub user. It locates the starred_url in the json, but there is an issue with the url and it is not found**

All other data is extracted

** username file is in .gitignore file, but it still shows in the repo. This is not a big deal as it is not sensitive information, but be sure to place in the .gitignore file before pushing to GitHub


