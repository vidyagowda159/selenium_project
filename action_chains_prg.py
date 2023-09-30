# send_keys(), click(), clear()

# doubleclick, hover, move to element, drag and drop, ctrl + a -> low level interactions -> action chains
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

path = r"C:\Users\Vidyashree M C\PycharmProjects\selenium_project\HTML files\demo.html"
driver.get(path)
driver.maximize_window()

action_obj = ActionChains(driver)
time.sleep(3)

button = driver.find_element("id", "double-click")

action_obj.double_click(button).perform()

# ----------------------------------------------------------------
# hovering action/ move to element
driver.get("https://www.meesho.com/")
driver.maximize_window()

action = ActionChains(driver)

kids_section = driver.find_element("xpath", '//span[text()="Kids"]')
action.move_to_element(kids_section).perform()

driver.find_element("xpath", '//p[text()="Soft Toys"]').click()

# -------------------------------------------------------------------
# keyboard simulations
driver.get("https://www.meesho.com/")
driver.maximize_window()
time.sleep(2)

action = ActionChains(driver)
action.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
action.send_keys(Keys.PAGE_UP).perform()
time.sleep(2)

action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(1)

element = driver.find_element("xpath", '//input[@placeholder="Try Saree, Kurti or Search by Product Code"]')
action.context_click(element).perform()

# ------------------------------------------------------------------------------------------------
# drag and drop
driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
driver.maximize_window()

source_element = driver.find_element("id", "draggable")
target_element = driver.find_element("id", "droppable")
time.sleep(2)
action = ActionChains(driver)
action.drag_and_drop(source_element, target_element).perform()

# flipkart.com --> Electronics --> Gaming --> click accessory kits




























