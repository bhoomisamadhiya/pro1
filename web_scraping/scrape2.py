import requests
from bs4 import BeautifulSoup

url = 'https://www.naukri.com/remote-jobs?src=discovery_trendingWdgt_homepage_srch'
response = requests.get(url)

print(response.status_code)
# print(response.content)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    print('inside if')
    
    job_listings = soup.find_all('article', class_='jobTuple')
    print('after job_listings')

    if job_listings:
        for jobs in job_listings:
            print('inside for')

            job_title = jobs.find('a', class_='Software engineer').text.strip()
            company_name = jobs.find('a', class_='python').text.strip()
            # job_location = jobs.find('li', class_='location').text.strip()
            # job_experience = jobs.find('li', class_='experience').text.strip()
        
            print("Title:", job_title)
            print("Company:", company_name)
            # print("Location:", job_location)
            # print("Experience:", job_experience)
            print("=" * 50)

    else:
        print('failed to retrieve the webpage.')
