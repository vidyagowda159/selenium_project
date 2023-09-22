# count the number of anchor tags in demo.html

import time
from selenium import webdriver

options_ = webdriver.ChromeOptions()
options_.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options_)

path = r"C:\Users\Vidyashree M C\PycharmProjects\selenium_project\HTML files\demo.html"

# driver.get(path)
# driver.maximize_window()

# element = driver.find_element("xpath", "//a")
# print(element)
# # find_element() returns only the first matching element in the webpage(returns a webelement)
#
# element = driver.find_elements("xpath", "//a")
# # find_elements() - returns all the matches in the form of list(list of webelements)
# print(len(element))
#
# element = driver.find_elements("tag name", "a")
# print(len(element))

#######################################################################################################
# fetch link texts in demo.html

# links = driver.find_elements("tag name", "a")   # links -> list (doesnot support any webelement methods)
#
# for link in links:          # link --> web element --> click(), send_keys(), is_enabled()
# 	print(link.text)
# 	print(link.get_attribute("href"))
#
#
# driver.close()

# ------------------------------------------------------------------------------------------
# selecting all the radio button in community poll

# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
#
# # radio_btns = driver.find_elements("css selector", 'input[type="radio"]')
#
# radio_btns = driver.find_elements("name", "pollanswers-1")
# print(len(radio_btns))
#
# for button in radio_btns:
# 	button.click()
# 	time.sleep(1)

######################################################################################################
# opening release notes of first 10 version from python.org

driver.get("https://www.python.org/downloads/")
driver.maximize_window()

links = driver.find_elements("xpath", '//a[text()="Release Notes"]')

for link in links[:10]:
	time.sleep(1)
	link.click()
	time.sleep(1)
	driver.back()

# capture the link text and the href attribute of the links which have "python" word in their link text


driver.close()




