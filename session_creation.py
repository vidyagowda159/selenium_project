"""
from selenium import webdriver

# adding extra capabilities using ChromeOptions class
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

# launch chrome browser/ create chrome session
driver = webdriver.Chrome(options=opts)
print(driver)
# <selenium.webdriver.chrome.webdriver.WebDriver (session="462b4e5b6a70ed751288578993581c02")>
"""

# create firefox browser session
from selenium import webdriver

driver = webdriver.Firefox()
print(driver)
# <selenium.webdriver.firefox.webdriver.WebDriver (session="fac61f2a-ec7f-435a-8421-58c8265f9d1b")>










