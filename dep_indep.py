import time

from selenium import webdriver

options_ = webdriver.ChromeOptions()
options_.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options_)

# driver.get("https://www.python.org/downloads/")
# driver.maximize_window()
# versions = ["Python 3.10.12", "Python 3.8.17", "Python 3.11.1"]
#
# for version in versions:
# 	element = driver.find_element("xpath", f'//a[text()="{version}"]/../..//a[text()=" Download"]')
# 	time.sleep(2)
# 	element.click()
# 	time.sleep(2)
# 	driver.back()

# driver.find_element("xpath", '//a[text()="Python 3.8.18"]/../..//a[text()=" Download"]').click()
# driver.find_element("xpath", '//a[text()="Python 3.8.18"]/../..//a[text()="Release Notes"]').click()

# # ---------------------------------------------------------------------------------------
# driver.get("https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market")
# driver.maximize_window()
# time.sleep(3)
#
# shares = ["ADANIPORTS", "COALINDIA", "TECHM", "BPCL", "POWERGRID"]
#
# for share in shares:
# 	element = driver.find_element("xpath", f'//a[text()="{share}"]/../..//td[7]')
# 	print(element.text)
#
# # print(driver.find_element("xpath", '//a[text()="ADANIPORTS"]/../..//td[7]').text)
# #
# # print(driver.find_element("xpath", '//a[text()="COALINDIA"]/../..//td[7]').text)
# #
# # print(driver.find_element("xpath", '//a[text()="TECHM"]/../..//td[7]').text)
#
# driver.close()

###########################################################################################
# click on all the checkboxes from demo.html language table
path = r"C:\Users\Vidyashree M C\PycharmProjects\selenium_project\HTML files\demo.html"

driver.get(path)
driver.maximize_window()


languages = ["Java", "Python", "Perl", "Ruby", "C#", "JavaScript"]

for language in languages:
	driver.find_element("xpath", f'//td[text()="{language}"]/..//input[@type="checkbox"]').click()
	time.sleep(1)

for language in languages[::-1]:
	driver.find_element("xpath", f'//td[text()="{language}"]/..//input[@type="checkbox"]').click()
	time.sleep(1)

#####################################################################################################
# fetch all the prices of dynamically changing webtable in demo.html

shares = ["AAPL", "MSFT", "AA", "FB"]

for share in shares:
	time.sleep(1)
	print(driver.find_element("xpath", f'//td[text()="{share}"]/..//td[@class="price"]').text)


driver.close()
# print(driver.find_element("xpath", '//td[text()="MSFT"]/..//td[@class="price"]').text)














