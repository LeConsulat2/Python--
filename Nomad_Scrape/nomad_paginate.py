import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
    print(f"Scrapping {url}...")#debugging(? why?)
    response = requests.get(url)

    #print(response.content)

    soup = BeautifulSoup(response.content, "html.parser",
    )

    jobs = soup.find("div", class_="jobList" ).find_all("div", class_ ="job-item")

    for job in jobs:
        title = job.find_all("span", class_="clicker-wrapper")
        location = job.find("span", class_ ="loc first").text
        field_of_work = job.find("span", class_="expertise").text

        print(title, "---------", location, "---------", field_of_work, "------\n")      
        all_jobs.append((title, location, field_of_work))

def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return len(soup.find("div", class_="pagination pagination-bottom").find_all("a", class_=""))

response = requests.get("https://careers.aut.ac.nz/search?page=0")
soup = BeautifulSoup(response.content, "html.parser")

buttons = len(soup.find("div", class_="pagination pagination-bottom").find_all("a", class_=""))

for x in range(buttons + 1):
    url = f"https://careers.aut.ac.nz/search?page={x}"
    print("request page", x)
    scrape_page(url)

print(len(all_jobs))    



#for button in buttons:
#     href_value = button['href']
#     print(f"Href: {href_value}")
#위 처럼 하면 , 밑처럼 결과 나옴
# Href: search?page=1
# Href: search?page=2
# Href: search?page=1
# Href: search?page=2
