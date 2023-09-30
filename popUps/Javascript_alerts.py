"""
alerts - popup that gets rendered/ popped up whenever user interacts with some elements
- alerts are not inspectable

to handle alerts
- switch the driver/ control to alert
- accept/ dismiss the alert
"""

import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# 1. simple alert
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

driver.find_element("css selector", 'input[value="Search"]').click()
time.sleep(2)
# switching the control to alert
alert_obj = driver.switch_to.alert

# handling the alert
print(alert_obj.text)
alert_obj.accept()
alert_obj.dismiss()

# -----------------------------------------------------------------------------
# 2. Confirmation alerts

driver.get("https://nxtgenaiacademy.com/alertandpopup/")
driver.maximize_window()

driver.find_element("xpath", '//button[text()="Confirm Alert Box"]').click()

time.sleep(2)
alert_obj = driver.switch_to.alert

# getting alert text
print(alert_obj.text)

# accept the alert
alert_obj.accept()

# dismiss the alert
alert_obj.dismiss()

# -------------------------------------------------------------------------------------------------
# 3. prompt alerts

driver.find_element("xpath", '//button[text()="Prompt Alert Box"]').click()

time.sleep(2)

# enter some text to the prompt alert
alert_obj = driver.switch_to.alert

alert_obj.send_keys("no")

# alert_obj.accept()
alert_obj.dismiss()




