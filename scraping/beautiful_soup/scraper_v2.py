import requests
from bs4 import BeautifulSoup
import csv
import json

URL = "https://www.python.org/jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Find the container that holds the job listings
jobs_container = soup.find("ol", class_="list-recent-jobs list-row-container menu")

# Find all job listings within the container
job_listings = jobs_container.find_all("li") if jobs_container else []


# Find all job listings that contain the word "Machine Learning" or "ML" in the title
ml_jobs = []
for job in job_listings:
    title_elem = job.find("h2", class_="listing-company")
    if title_elem and ("machine learning" in title_elem.text.lower() or "ml" in title_elem.text.lower()):
        job_link_url = job.find("a")["href"]
        ml_jobs.append((title_elem.text.strip(), job_link_url))


# Print the job title and link for each Machine Learning job
print("ML Jobs found:", len(ml_jobs))
print("ML Jobs found:")
for job_title, job_link in ml_jobs:
    print(job_title)
    print(f"Apply here: https://www.python.org/{job_link}\n")


# Save the ML jobs to a CSV file
with open("ml_jobs.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Job Title", "Job Link"])
    for job_title, job_link in ml_jobs:
        writer.writerow([job_title, f"https://www.python.org/{job_link}"])


# Save the ML jobs to a JSON file
ml_jobs_data = [
    {"title": job_title, "link": f"https://www.python.org/{job_link}"}
    for job_title, job_link in ml_jobs
]
with open("ml_jobs.json", "w", encoding="utf-8") as jsonfile:
    json.dump(ml_jobs_data, jsonfile, ensure_ascii=False, indent=2)
