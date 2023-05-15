from selenium import webdriver
#this package is used to hit actions of special keys like return or shift
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver =webdriver.Chrome('./chromedriver')

driver.get("https://www.python.org")

print(driver.title)

#accessing searcch bar of the python web page using dom
#and we know that its search bar name is 'q'
searchbar=driver.find_element_by_name("q")

#other ways to access this search bar
'''
<input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" >

using Id: .find_element_by_id(“id-search-field”)
 using xpath: .find_element_by_xpath(“//input[@id=’id-search-field’]”)
using class name: .find_element_by_class_name(“search-field”)
'''

searchbar.clear()
searchbar.send_keys("getting started with python")
#emulating press enter behaviour
searchbar.send_keys(Keys.RETURN)

print(driver.current_url)

#to close the browser
driver.close()

# window handle will uniquely identifies all open windows
driver.window_handles

#switch control to new window
driver.switch_to_window('window_name')

#switch control to a frame in given window
driver.switch_to_frame('framename')

# switch back to primary window
driver.switch_to_default_content()

#provide waiting time
#there are two types of wait
# explicit: where app wait until a component ready
#for explicit case we write it inside try catch, becoz it amy be possible that content is not loaded
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "id-of-new-element")))
finally:
    driver.quit()

#implicit :app wait only for given time
driver.implicitly_wait(5)
element = driver.find_element_by_id("id-of-new-element")


