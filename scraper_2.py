from bs4 import BeautifulSoup

# Replace this with the actual HTML content you obtained from the website
html_content = """
<ul class="jobs-list-items">
    <li class="bjs-jlid">
        <div class="bjs-jlid__wrapper">
            <div class="bjs-jlid__header">
                <div class="bjs-jlid__meta">
                    <h4 class="bjs-jlid__h"><a href="https://berlinstartupjobs.com/engineering/senior-frontend-engineerin-flutter-m-w-d-mindful/">Senior Frontend Engineer:in – Flutter (m/w/d)</a></h4>
                    <a class="bjs-jlid__b" href="https://berlinstartupjobs.com/companies/mindful/">Mindful</a>
                </div>
            </div>
        </div>
    </li>
    <!-- Add more job listings if needed -->
</ul>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Extracting job details
job_listings = soup.find_all('li', class_='bjs-jlid')

for job_listing in job_listings:
    # Assuming there are multiple h4 elements with class 'bjs-jlid__h' inside each job listing
    # Extracting job details
    job_titles = job_listing.select('h4.bjs-jlid__h a')
    job_title = job_titles[0].text.strip() if job_titles else ""

    company_names = job_listing.select('a.bjs-jlid__b')
    company_name = company_names[0].text.strip() if company_names else ""

    description_wrappers = job_listing.select('div.bjs-jlid__wrapper > div')
    description = description_wrappers[0].text.strip() if description_wrappers else ""

    job_links = job_listing.select('h4.bjs-jlid__h a')
    job_link = job_links[0]['href'] if job_links else ""


    print(f"Job Title: {job_title}")
    print(f"Company Name: {company_name}")
    print(f"Description: {description}")
    print(f"Job Link: {job_link}")
    print("\n")
