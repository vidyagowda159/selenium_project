import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element("xpath", '//a[text()="Create new account"]').click()

date_listbox = driver.find_element("id", "day")
date_obj = Select(date_listbox)

month_listbox = driver.find_element("name", "birthday_month")
month_obj = Select(month_listbox)

year_listbox = driver.find_element("css selector", 'select[title="Year"]')
year_obj = Select(year_listbox)

date_obj.select_by_visible_text("3")
month_obj.select_by_value("10")
year_obj.select_by_index(4)





