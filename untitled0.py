#import two library 
# BeautifulSoup and requests
from bs4 import BeautifulSoup
import requests

#set the website url address in url variable
url = "https://boston.craigslist.org/search/sof"
#set the web page in response variable
response = requests.get(url)
#response print 200 that means everything is OK
print(response)
#extract the source code of the webpage 
# and keep it in data variable
data = response.text
#data is printing the full source code
# of the website
print(data)
#
soup = BeautifulSoup(data, 'html.parser')
#find all the <a href=""></a> tags 
# from the html code and
# keep these in tags variable 
tags = soup.find_all('a')
#tags is printing all the <a href=""></a> links
print(tags)
#clean all the links from the code and print
for tag in tags:
    print(tag.get('href'))
    

#find all the <a href=""></a> tags
# which has a class name called result-title
# from the html code and
# keep these in title variable 
titles = soup.find_all('a', {"class":"result-title"})
#clean all the links from the code and print
for title in titles:
    print(title.text)


#print job details

#find all the p tags
# which has a class name called result-info
# from the html code and
# keep these in jobs variable 
jobs = soup.find_all('p', {'class':'result-info'})
#iterate all the jobs one by one
for job in jobs:
    #find the text in <a href=""></a> tags
    # which has a class name called result-title
    # from the html code and
    # keep these in title variable 
    title = job.find('a', {'class':'result-title'}).text
    #find the span tags
    # which has a class name called result-hood
    # from the html code and
    # keep these in location_tag variable    
    location_tag = job.find('span', {'class':'result-hood'})
    #check if location_tag exist or not
    location = location_tag.text[2:-1] if location_tag else 'N/A'
    #find the text in time tags
    # which has a class name called result-date
    # from the html code and
    # keep these in date variable
    date = job.find('time', {'class':'result-date'}).text
    #find the link in <a href=""></a> tags
    # which has a class name called result-title
    # from the html code and
    # keep these in link variable
    link = job.find('a', {'class':'result-title'}).get('href')
    print("Job Title: ", title, "\nLocation: ", location, "\nDate: ", date, "\nLink: ", link, "\n-----")
