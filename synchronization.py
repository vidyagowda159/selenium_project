import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

path = r"C:\Users\Vidyashree M C\PycharmProjects\selenium_project\HTML files\loading.html"
driver.get(path)
driver.maximize_window()

# # unconditional synchronization - unconditionally making the interpreter to wait
# # time.sleep(timeout)
# time.sleep(20)
#
# # send the keys to first name textfield
# driver.find_element("name", "fname").send_keys("Steve")

# conditional synchronization - makes the webdriver wait based on certain condition
# 1. implicit wait(timeout)
# 2. explicit wait/ webdriver wait


# #  implicit wait() - condition will be assumed internally/ implicitly by the webdriver
# # - applicable only on find_element() & find_elements()
# # polling frequency - the time in which the task is repeatedly done(500 ms)
# driver.implicitly_wait(30)      # initializing driver with implicit wait time of 30 seconds
#
# # send the keys to first name textfield
# driver.find_element("name", "fname").send_keys("Steve")
# driver.find_element("name", "lname").send_keys("jobs")

# --------------------------------------------------------------------------------------------
# explicit wait/webdriver wait

# import WebDriverWait class
from selenium.webdriver.support.ui import WebDriverWait

# import expected conditions
from selenium.webdriver.support import expected_conditions as EC

wait_ = WebDriverWait(driver, 60)
locator = ("name", "fname")

# true --> web element whose locator has been passed, false -> TimeOutException
# first_name_element = wait_.until(EC.presence_of_element_located(locator))

first_name_element = wait_.until(EC.visibility_of_element_located(locator))

# web_element = driver.find_element("name", "fname")
# first_name_element = wait_.until(EC.visibility_of(web_element))

# driver.find_element("name", "fname").send_keys("Steve")
first_name_element.send_keys("steve")

# ----------------------------------------------------------------------------------------------------
# waiting until the loading symbol becomes invisible

# wait until the progress bar reaches 100%, once it reaches click on the button to restart the progress










