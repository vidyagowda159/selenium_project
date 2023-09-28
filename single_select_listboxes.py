# Select class --> standard listboxes (created using select tag)
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

path = r"C:\Users\Vidyashree M C\PycharmProjects\selenium_project\HTML files\demo.html"
driver.get(path)
driver.maximize_window()

# locate the listbox/ select element
listbox_element = driver.find_element("id", "standard_cars")

# create an object of Select class
select_obj = Select(listbox_element)

# # select an option
#
# # 1. select_by_visible_text()
# select_obj.select_by_visible_text("Land Rover")
# time.sleep(2)
#
# select_obj.select_by_visible_text("Audi")
# time.sleep(2)
#
# # 2. select_by_value()
# select_obj.select_by_value("bmw")
# time.sleep(2)
#
# select_obj.select_by_value("nin")
# time.sleep(2)
#
# # 3. select_by_index()
# select_obj.select_by_index(5)

# # returns list of all the options webelements
# all_options = select_obj.options
#
# # selecting all the options one by one
# for option in all_options:
# 	text = option.text
# 	select_obj.select_by_visible_text(text)
# 	time.sleep(1)
#
# print(select_obj.is_multiple)      # None
#
# print(select_obj.first_selected_option.text)        # return the current selected option


# selecting all the options using select_by_index and select_by_value

# get all the options
all_options = select_obj.options

# # select_by_value()
# for option in all_options:
# 	result = option.get_attribute("value")
# 	select_obj.select_by_value(result)
# 	time.sleep(1)

# select_by_index()
# for index, option in enumerate(all_options):
# 	select_obj.select_by_index(index)
# 	time.sleep(1)

for index in range(len(all_options)):
	select_obj.select_by_index(index)
	time.sleep(1)

driver.close()




