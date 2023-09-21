"""
css selectors: allows to locate any element using any attribute

syntax: tagname[attr_name=attr_value]

input[value="Search store"]

"""

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

# driver.find_element("css selector", 'input[value="Search store"]').send_keys("books")
driver.find_element("css selector", 'a[class="ico-register"]').click()

# https://demo.actitime.com/login.do

