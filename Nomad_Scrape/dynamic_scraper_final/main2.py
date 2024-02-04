from bs4 import BeautifulSoup
import csv
import requests

class Job:
    def __init__(self, title, location, job_type, link):
        self.title = title
        self.location = location
        self.job_type = job_type
        self.link = link

class JobsScraper:
    def __init__(self, keyword):
        self.keyword = keyword
        self.jobs = []

    def get_content(self):
        url = f"https://careers.aut.ac.nz/{self.keyword}"  # Update with your actual URL
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch content. Status code: {response.status_code}")
            return ""

    def scrape_jobs(self):
        content = self.get_content()

        if not content:
            print("Content retrieval failed.")
            return

        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="job-item")

        for job in jobs:
            link = f"https://careers.aut.ac.nz/{job.find('a')['href']}"
            title_span = job.find("span", class_="clicker-wrapper")
            title = title_span.text.strip() if title_span else "N/A"
            location = job.find("span", class_="loc first").text
            job_type = job.find("span", class_="work-type last").text

            job_obj = Job(title, location, job_type, link)
            self.jobs.append(job_obj)

    def save_to_file(self):
        file_path = f"{self.keyword}_jobs.csv"
        with open(file_path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Location", "Type", "Link"])

            for job in self.jobs:
                writer.writerow([job.title, job.location, job.job_type, job.link])

        print(f"CSV file saved: {file_path}")

if __name__ == "__main__":
    keywords = ["your", "keywords", "here"]  # Replace with your desired keywords

    for keyword in keywords:
        scraper = JobsScraper(keyword)
        scraper.scrape_jobs()
        scraper.save_to_file()
