from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from file import save_to_file
import time
import csv

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://careers.aut.ac.nz/search?page=0")

time.sleep(5)

# Click on the input field within the formLabel class
page.click("button.sh_Button")

time.sleep(5)

# Wait for the input field to be present
page.wait_for_selector("#jobSearchKeywordsTextField")

# Use page.fill to fill in the input field
page.fill("#jobSearchKeywordsTextField", "manager")

time.sleep(2)  # Adjust the sleep time if needed

# Press the "Enter" key
page.press("#jobSearchKeywordsTextField", "Enter")

time.sleep(10)

# Scroll to the end of the page using JavaScript
#

#time.sleep(5)

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="job-item")

jobs_db = []

for job in jobs:
    link = f"https://careers.aut.ac.nz/{job.find('a')['href']}"

    # Check if the span with class "clicker-wrapper" is found
    title_span = job.find("span", class_="clicker-wrapper")
    title = title_span.text.strip() if title_span else "N/A"

    location = job.find("span", class_="loc first").text
    type = job.find("span", class_="work-type last").text

    job_data = {
        "title": title,
        "location": location,
        "type": type,
        "link": link
    }
    jobs_db.append(job_data)

print(jobs_db)
print(len(jobs_db))

file = open("jobs.csv", "w")
writer = csv.writer(file)
writer.writerow(["Title", "Location", "Type", "Link"])

for job in jobs_db:
    writer.writerow(job.values())

save_to_file(keyword, jobs)    