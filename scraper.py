import requests
from requests import get
import random
from bs4 import BeautifulSoup

movie_ids = [
    238,
    680,
    550,
    185,
    641,
    515042,
    152532,
    120467,
    872585,
    906126,
    840430,
    7801230
]

for movie in movie_ids:
    url = f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie}"
    response = requests.get(url)

    if response.status_code == 200:
       data = response.json()
       title = data.get("title")
       overview = data.get("overview")
       vote_average = data.get("vote_average")

       print(f"Movie: {movie}" 
             f"Title: {title}"
            f"Overview: {overview}" 
             f"Vote Average: {vote_average}")
    else:
       print(f"Failed to fetch details for Movie ID {movie}. Status Code: {response.status_code}")





# url = "https://careers.aut.ac.nz/search?search=cvid-faZd7"
# random_number =random.randint(1,9999999)
# response = requests.get(url, headers = {'user-agent': f'{random_number}'})
# html = response.content
# soup = BeautifulSoup(html, 'html.parser')
# #parser - idea of taking huge data organising into tags#
# a_tags = soup.find_all('a')

# for a_tag in a_tags:
#    print(a_tag) 