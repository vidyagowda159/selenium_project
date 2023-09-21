import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
#
# driver.find_element("css selector", 'a[class="ico-register"]').click()
# time.sleep(1)
# driver.find_element("css selector", 'input[value="F"]').click()
# time.sleep(1)
# driver.find_element("css selector", 'input[id="FirstName"]').send_keys("John")
# time.sleep(1)
# driver.find_element("css selector", 'input[name="LastName"]').send_keys("Doe")
# time.sleep(1)
# driver.find_element("css selector", 'input[name="Email"]').send_keys("john@gmail.com")
# time.sleep(1)
# driver.find_element("css selector", 'input[id="Password"]').send_keys("john123")
# time.sleep(1)
# driver.find_element("css selector", 'input[id="ConfirmPassword"]').send_keys("john123")
# time.sleep(1)

# ---------------------------------------------------------------------------------------------
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()

driver.find_element("css selector", 'input[placeholder="Username"]').send_keys("admin")
time.sleep(1)
driver.find_element("css selector", 'input[name="pwd"]').send_keys("manager")
time.sleep(1)
driver.find_element("css selector", 'a[id="loginButton"]').click()

driver.close()










