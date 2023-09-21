from selenium import webdriver

options_ = webdriver.ChromeOptions()
options_.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options_)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

# # using class attribute
# driver.find_element("xpath", '//a[@class="ico-register"]').click()

# using text()
driver.find_element("xpath", '//a[text()="Register"]').click()

# # using name attribute
# driver.find_element("xpath", '(//input[@name="Gender"])[1]').click()

driver.find_element("xpath", '//input[@value="M"]').click()

driver.find_element("xpath", '//input[@name="FirstName"]').send_keys("Steve")

driver.find_element("xpath", '//input[@id="LastName"]').send_keys("Jobs")

driver.find_element("xpath", '//input[@id="Email"]').send_keys("steve.jobs@gmail.com")

driver.find_element("xpath", '//input[@id="Password"]').send_keys("steve123")

driver.find_element("xpath", '//input[@id="ConfirmPassword"]').send_keys("steve123")




