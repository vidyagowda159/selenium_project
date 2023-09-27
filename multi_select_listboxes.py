import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

path = r"C:\Users\Vidyashree M C\PycharmProjects\selenium_project\HTML files\demo.html"
driver.get(path)
driver.maximize_window()

element = driver.find_element("id", "multiple_cars")

s_obj = Select(element)

s_obj.select_by_index(3)
time.sleep(1)
s_obj.select_by_visible_text("Audi")
time.sleep(1)
s_obj.select_by_value("bmw")
time.sleep(1)


# s_obj.deselect_all()
# s_obj.deselect_by_value("aud")
# time.sleep(1)
# s_obj.deselect_by_index(2)
# time.sleep(1)
# s_obj.deselect_by_visible_text("Ford")

# get only selected options
sel_options = s_obj.all_selected_options      # list of selected options webelement

for option in sel_options:
	print(option.text)

print(s_obj.first_selected_option.text)     # return the option present at first index in all_selected_options

print(s_obj.is_multiple)        # True

driver.close()

# facebook.com --> create account --> fill the sign up form
# https://www.facebook.com/nopCommerce
