from selenium import webdriver
from selenium.webdriver.common.by import By

"""""
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
"""""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

events_time_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li time")
events_name_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li a")
events = {}
for event in range(len(events_time_list)):
    events[event] = {
        "time": events_time_list[event].text,
        "name": events_name_list[event].text
    }


driver.quit()
print(events)
