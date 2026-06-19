from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs")

input("Login manually and press Enter...")

jobs = [
    ["Python Developer", "TCS", "Bangalore"],
    ["Software Engineer", "Infosys", "Hyderabad"],
    ["Backend Developer", "Wipro", "Pune"],
    ["Python Developer", "TCS", "Bangalore"],
    ["Data Analyst", "Accenture", "Chennai"],
    ["Software Engineer", "Infosys", "Hyderabad"]
]

cards = driver.find_elements(By.CLASS_NAME, "base-search-card")

for card in cards:

    try:
        title = card.find_element(
            By.CLASS_NAME,
            "base-search-card__title"
        ).text

        company = card.find_element(
            By.CLASS_NAME,
            "base-search-card__subtitle"
        ).text

        location = card.find_element(
            By.CLASS_NAME,
            "job-search-card__location"
        ).text

        jobs.append([
            title,
            company,
            location
        ])

    except:
        pass


df = pd.DataFrame(
    jobs,
    columns=[
        "Job Title",
        "Company",
        "Location"
    ]
)

df.drop_duplicates(inplace=True)

df.to_csv(
    "jobs.csv",
    index=False
)

print("Data Saved!")

driver.quit()