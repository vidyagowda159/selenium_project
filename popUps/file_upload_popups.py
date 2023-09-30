import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element("xpath", '//div[contains(text(), "Upload Resume")]').click()

# locate the element with input tag with type="file" attribute
path = r"C:\Users\Vidyashree M C\PycharmProjects\selenium_project\notes\dep-independent xpaths.txt"
driver.find_element("xpath", '//input[@type="file"]').send_keys(path)








