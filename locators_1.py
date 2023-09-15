import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

# launch the demo web shop application
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

# locate search bar in demowebshop home page

# using id locator
search_bar = driver.find_element("id", "small-searchterms")
print(search_bar)

# using class locator
search_bar = driver.find_element("class name", "search-box-text.ui-autocomplete-input")
print(search_bar)

# using name locator
search_bar = driver.find_element("name", "q")
print(search_bar)

# web element methods

# type something
search_bar.send_keys("mobiles")
time.sleep(3)

# clears the previous text
search_bar.clear()
time.sleep(3)

# position and size of the web element
print(search_bar.location)          # {x:, y: }
print(search_bar.size)              # {width:, height: }
print(search_bar.rect)              # {width:, height: , x:, y: }

# get the attribute values
print(search_bar.get_attribute("class"))
print(search_bar.get_attribute("autocomplete"))
print(search_bar.get_attribute("type"))

# boolean methods
print(search_bar.is_displayed())
print(search_bar.is_enabled())
print(search_bar.is_selected())

print(search_bar.tag_name)

# click on the element
search_bar.click()
time.sleep(3)

driver.close()
