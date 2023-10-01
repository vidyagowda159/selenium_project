import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

path = r"C:\Users\Vidyashree M C\PycharmProjects\selenium_project\HTML files\iframe.html"
driver.get(path)
driver.maximize_window()
driver.implicitly_wait(10)

# switch to the frame

# # frame name - name attribute
# driver.switch_to.frame("frame1")

# # frame id - id attribute
# driver.switch_to.frame("FR1")

# # frame index
# driver.switch_to.frame(0)

# frame web element using any locator
element = driver.find_element("xpath", "(//iframe)[1]")
driver.switch_to.frame(element)

driver.find_element("name", "q").send_keys("Books")

# switch back to parent frame
# driver.switch_to.parent_frame()         # switches back to the immediate parent

driver.switch_to.default_content()      # switches back to the main frame

# switching to tricentis frame
driver.switch_to.frame("FR2")
driver.find_element("id", "search_form").send_keys("abc")

"""
parent
	iframe1
		iframe2
			iframe3
			
"""

"""
alerts, windows, iframes --> driver.switch_to
- alerts -> alert
- windows -> window(window_id)
- iframes -> frame(name/ id/ index/ webelement)

# redbus website --> login 
"""





