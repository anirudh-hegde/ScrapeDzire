from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time


def scrape_data():
    # Download versions of chromedriver and chrome which are compatible
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    # webdriver to interact with the browser on client side
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    driver.get("https://mlh.io/seasons/2024/events")

    links = driver.find_elements(By.CLASS_NAME, "event-link")  # Fetching links of hackathon websites
    images = driver.find_elements(By.CSS_SELECTOR, ".image-wrap img")  # Fetching images of hackathons
    names = driver.find_elements(By.CLASS_NAME, "event-name")  # Fetching names of hackathons
    dates = driver.find_elements(By.CLASS_NAME, "event-date")  # Fetching dates
    locs = driver.find_elements(By.CLASS_NAME, "event-location")  # Fetching location
    modes = driver.find_elements(By.CLASS_NAME, "event-hybrid-notes")  # Fetching modes

    hackathons = []

    for i in range(len(links)):
        hackathon = {
            "name": names[i].text,
            "link": links[i].get_attribute("href"),
            "image": images[i].get_attribute("src"),
            "date": dates[i].text,
            "location": locs[i].text,
            "mode": modes[i].text
        }
        hackathons.append(hackathon)

    # save your json file in your preferred destination
    with open("/home/anirudh/Downloads/mlh-hackathons.json", "w") as f:
        json.dump(hackathons, f, indent=4);
    driver.quit()

    print(f"Saving data to: /home/anirudh/Downloads/mlh-hackathons.json")
    exit()


while (1):
    scrape_data()
