from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# to fix the problem in race condition where the 
# find element is executing before the it is present on the page
driver.implicitly_wait(10) # seconds

driver.get("http://www.python.org")
assert "Python" in driver.title

# driver.find_element_by_xpath("//*[@id='udemy']/div[2]/div[2]/div[1]/div[4]/div[6]/div/button").click()

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()


