from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time
from selenium.webdriver.common.keys import Keys

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/")

"""
Signing in 
"""
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
time.sleep(2)
first_name = driver.find_element(By.XPATH, value="/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input")
first_name.send_keys(EMAIL)
time.sleep(2)

name = driver.find_element(By.NAME, value="session_password")
name.send_keys(PASSWORD)

time.sleep(2)
submit_button = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/button")
submit_button.click()
time.sleep(10)

"""
searching for jobs
"""

job_link = driver.find_element(By.XPATH, "/html/body/div[6]/header/div/nav/ul/li[3]/a")
time.sleep(2)
job_link.click()

time.sleep(2)

job_search = driver.find_element(By.ID, "recentSearchesIndex__0")
print(job_search.text)
job_search.click()
time.sleep(2)

for i in range(6):
    time.sleep(2)
    jobs_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    print(len(jobs_list))
    driver.execute_script("arguments[0].scrollIntoView();", jobs_list[0])
    time.sleep(5)
    for card in jobs_list:
        try:
            card.click()
            print(f"Job clicked")
            time.sleep(2)
        except StaleElementReferenceException:
            print("Stale element reference. Skipping.")

driver.quit()
