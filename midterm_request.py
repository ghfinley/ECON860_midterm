#                                      Request program to obtain the html 

# import packages
import urllib.request
import os 
import time
import datetime

# Create file path 
if not os.path.exists("html_files"): 
	os.mkdir("html_files") 

# Request html
for i in range(10):
	current_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S") #use the datetime command to get the time stamp all in numbers (YearMonthDayHourMiniuteSecond)
	print(current_time) #print the current time, this will show that something is printing in the for loop as good practice 
	f = open("html_files/GitHub_Users" + current_time + ".html","wb",) 
	response = urllib.request.urlopen("http://45.79.253.243/index.html") 
	html = response.read() 
	f.write(html) 
	f.close() 
	time.sleep(30)

	



