# monster india --> skill tests --> click python

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.foundit.in/")
# driver.maximize_window()
#
# action_obj = ActionChains(driver)
#
# # //a[contains(text(), "Skill Tests")]
# skill_tests = driver.find_element("partial link text", "Skill Tests")
#
# action_obj.move_to_element(skill_tests).perform()
# time.sleep(2)
# driver.find_element("xpath", '//h4[text()=" Back-end Developer "]/..//a[contains(text(), "Python")]').click()

#######################################################################################################
driver.get("https://www.flipkart.com/")
driver.maximize_window()

action = ActionChains(driver)

electronics = driver.find_element("xpath", '//span[text()="Electronics"]')

# closing the modal window
driver.find_element("xpath", '//span[text()="✕"]').click()
time.sleep(2)

# hovering on electronics section
action.move_to_element(electronics).perform()

# hovering on gaming sub section
gaming = driver.find_element("xpath", '//a[text()="Gaming"]')
time.sleep(2)
action.move_to_element(gaming).perform()

# clicking accessory kits in gaming sub section
driver.find_element("xpath", '//a[text()="Accessory Kits"]').click()









