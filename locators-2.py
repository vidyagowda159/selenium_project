# link text locator

from selenium import webdriver

options_ = webdriver.ChromeOptions()
options_.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options_)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

# driver.find_element("link text", "Log in").click()
# driver.find_element("link text", "Register").click()

# driver.find_element("partial link text", "Books").click()

# driver.find_element("partial link text", "Log").click()

