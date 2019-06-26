from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://boston.craigslist.org/search/sof'

npo_jobs = {}
job_no = 0
while True:
    
    response = requests.get(url)

    data = response.text
    
    soup = BeautifulSoup(data, 'html.parser')
    
    jobs = soup.find_all('p', {'class':'result-info'})
    
    for job in jobs:
        title = soup.find('a', {'class':'result-title'}).text
        location_tag = soup.find('span', {'class':'result-hood'})
        location = location_tag.text if location_tag else 'N/A'
        date = soup.find('time', {'class':'result-date'}).text
        link = soup.find('a', {'class':'result-title'}).get('href')
        
        job_response = requests.get(link)
        job_data = job_response.text
        job_soup = BeautifulSoup(job_data, 'html.parser')
        job_description = job_soup.find('section', {'id':'postingbody'}).text
        job_attribute_tag = job_soup.find('p', {'class':'attrgroup'})
        job_attribute = job_attribute_tag.text if job_attribute_tag else 'N/A'
        
        job_no += 1
        npo_jobs[job_no] = [title, location, date, link, job_attribute, job_description]
        print("Title: ", title, "\nLocation: ", location, "\nDate: ", date, "\nLink: ", link, "\nJob Description: ", job_description, "\nJob Attribute: ",job_attribute, "\n----------",)
    
    url_tag = soup.find('a',{'title':'next page'})
    
    if url_tag.get('href'):
        url = 'https://boston.craigslist.org' + url_tag.get('href')
        print(url)
    else:
        break

print("Total Jobs: ", job_no)
#Specify orient='index' to create the DataFrame using dictionary keys as rows:
#When using the ‘index’ orientation, the column names can be specified manually:
npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient = 'index', columns = ['title', 'location', 'date', 'link', 'job_attribute', 'job_description'] )

npo_jobs_df.head()

npo_jobs_df.to_csv('npo_jobs.csv')