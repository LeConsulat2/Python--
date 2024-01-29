import requests
import random
from bs4 import BeautifulSoup

url = "https://careers.aut.ac.nz/search?search=cvid-faZd7"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

# List of class names representing dates to extract
date_types = ['post-date', 'close-date']

for date_type in date_types:
    dates = soup.find_all('span', class_=date_types)
    print(f"Text content for date class '{date_type}':")
    
    for date in dates:
        print(date.get_text(strip=True))
    
   
 


# #parser - idea of taking huge data organising into tags#
# a_tags = soup.find_all('a')

# for a_tag in a_tags:
#    print(a_tag) 