from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    job_listings = []

    # Extracting information from each job listing on the page
    job_list_items = soup.find("ul", class_="jobs-list-items")
    if job_list_items:
        for job_meta in job_list_items.find_all("li", class_="ais-Hits-item"):
            header = job_meta.find("div", class_="bjs-jlid__header")
            if header:
                company = header.find("span", class_="company").text.strip()
                title = header.find("h2").text.strip()
                description = job_meta.find("div", class_="description").text.strip()
                link = job_meta.find("a", class_="view-job-button")["href"]

                job_info = {
                    "company": company,
                    "title": title,
                    "description": description,
                    "link": link
                }

                job_listings.append(job_info)

    return job_listings

def scrape_berlin_startup_jobs(base_url, num_pages=None):
    all_job_listings = []

    for page in range(1, num_pages + 1) if num_pages else [1]:
        page_url = f"{base_url}/page/{page}" if page > 1 else base_url
        job_listings = scrape_page(page_url)
        all_job_listings.extend(job_listings)

    return all_job_listings

def scrape_weworkremotely(search_term):
    base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
    url = f"{base_url}{search_term}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    job_listings = []

    # Extracting information from each job listing on the page
    for job_meta in soup.find_all("li", class_="feature"):
        company = job_meta.find("span", class_="company").text.strip()
        title = job_meta.find("span", class_="title").text.strip()
        link = "https://weworkremotely.com" + job_meta.find("a")["href"]

        job_info = {
            "company": company,
            "title": title,
            "link": link
        }

        job_listings.append(job_info)

    return job_listings

def scrape_web3_career(search_term):
    base_url = "https://web3.career/-jobs"
    url = f"{base_url}/{search_term}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    job_listings = []

    # Extracting information from each job listing on the page
    for job_meta in soup.find_all("div", class_="job-item"):
        company = job_meta.find("span", class_="company").text.strip()
        title = job_meta.find("h2").text.strip()
        link = "https://web3.career" + job_meta.find("a")["href"]

        job_info = {
            "company": company,
            "title": title,
            "link": link
        }

        job_listings.append(job_info)

    return job_listings

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search_term = request.form["search_term"].lower()

        berlin_startup_jobs = scrape_berlin_startup_jobs(f"https://berlinstartupjobs.com/skill-areas/{search_term}")
        weworkremotely_jobs = scrape_weworkremotely(search_term)
        web3_career_jobs = scrape_web3_career(search_term)

        return render_template("index.html",
                               search_term=search_term,
                               berlin_startup_jobs=berlin_startup_jobs,
                               weworkremotely_jobs=weworkremotely_jobs,
                               web3_career_jobs=web3_career_jobs)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
