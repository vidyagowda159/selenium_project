from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://demo.actitime.com/login.do")
expected_title = "actiTIME - Enter Time-Track"

# login
driver.find_element("name", "username").send_keys("admin")
driver.find_element("name", "pwd").send_keys("manager")
driver.find_element("xpath", '//div[text()="Login "]').click()

# explicit wait until the title changes
wait_ = WebDriverWait(driver, 10)
wait_.until(EC.title_is(expected_title))

current_title = driver.title
print(current_title)

if current_title == expected_title:
	print("title matched")
else:
	print("titles not matched")

driver.close()


