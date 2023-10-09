from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
print(count.text)
all_portals = driver.find_element(By.LINK_TEXT, "free")
# all_portals.click()

search = driver.find_element(By.ID, value="#p-search")
search.send_keys("python")
search.send_keys(Keys.ENTER)
# driver.quit()
