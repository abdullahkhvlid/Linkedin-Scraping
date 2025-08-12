from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Setup Chrome options
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)

# Login to LinkedIn
driver.get("https://www.linkedin.com/login")
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
username.clear()
username.send_keys("your_email_here")  # Replace with your actual email
password.clear()
password.send_keys("your_password_here")  # Replace with your actual password
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)

# Go to job search page
search_query = "data science"
driver.get(f"https://www.linkedin.com/jobs/search/?keywords={search_query}")
time.sleep(5)

# Locate the left job list container
job_list = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "ul.jobs-search__results-list"))
)

# Scroll the job list container until at least 25 jobs are loaded or max scrolls reached
jobs_loaded = 0
scroll_attempt = 0
max_scroll_attempts = 15

while jobs_loaded < 25 and scroll_attempt < max_scroll_attempts:
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", job_list)
    time.sleep(2)
    job_cards = driver.find_elements(By.CSS_SELECTOR, "ul.jobs-search__results-list li")
    jobs_loaded = len(job_cards)
    scroll_attempt += 1

# Now scrape job cards (limit to 25)
jobs_data = []

for card in job_cards[:25]:
    try:
        title = card.find_element(By.CSS_SELECTOR, "h3").text.strip()
    except:
        title = None
    try:
        company = card.find_element(By.CSS_SELECTOR, "h4").text.strip()
    except:
        company = None
    try:
        location = card.find_element(By.XPATH, ".//span[contains(@class, 'location')]").text.strip()
    except:
        location = None
    try:
        date_posted = card.find_element(By.TAG_NAME, "time").get_attribute("datetime")
    except:
        date_posted = None
    
    jobs_data.append({
        "Title": title,
        "Company": company,
        "Location": location,
        "Date Posted": date_posted,
    })

# Save to Excel
df = pd.DataFrame(jobs_data)
df.to_excel("linkedin_jobs_25.xlsx", index=False)

print(f"Saved {len(jobs_data)} jobs to linkedin_jobs_25.xlsx")

driver.quit()
