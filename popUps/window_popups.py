import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element("link text", "Facebook").click()

# get all the window handles/ window ids
handles = driver.window_handles
print(handles)              # [Demo web shop, Facebook]

# print the titles of each handle
for handle in handles:
	driver.switch_to.window(handle)
	print(driver.title)         # returns the active window's title

# close the modal popup in facebook window(child window)
driver.switch_to.window(handles[1])
driver.find_element("xpath", '//div[@aria-label="Close"]').click()
driver.find_element("name", "email").send_keys("abc@gmail.com")

driver.close()  # close current active window (Facebook)

# switching back to parent window
driver.switch_to.window(handles[0])
print(driver.title)

######################################################################################
# close only the parent window

# get all the window handles
handles = driver.window_handles         # [parent_id, child_id]

driver.switch_to.window(handles[0])
driver.close()

# close only the child window --> handles[1]

# booking.com --> sign in using google













