import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

register_link = driver.find_element("class name", "ico-register")
register_link.click()
time.sleep(2)

female_radio_button = driver.find_element("id", "gender-female")
female_radio_button.click()
time.sleep(2)
# male_radio_btn = driver.find_element("name", "Gender")
# male_radio_btn.click()

first_name = driver.find_element("id", "FirstName")
first_name.send_keys("Eve")
time.sleep(2)

# driver.find_element("id", "FirstName").send_keys("Eve")

last_name = driver.find_element("name", "LastName")
last_name.send_keys("John")
time.sleep(2)

# driver.find_element("name", "LastName").send_keys("John")

email = driver.find_element("id", "Email")
email.send_keys("eve123@gmail.com")
time.sleep(2)

pwd = driver.find_element("id", "Password")
pwd.send_keys("eve123")
time.sleep(2)

confirm_pwd = driver.find_element("name", "ConfirmPassword")
confirm_pwd.send_keys("eve123")

