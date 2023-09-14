import time
from selenium import webdriver

# create chrome session
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

# navigate to an url
driver.get("https://demowebshop.tricentis.com/")

# interacting with browser window
driver.maximize_window()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.fullscreen_window()

# navigating to previous and next pages
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()

# extract the size and position of the browser
print(driver.get_window_position())        # {x: , y: }
print(driver.get_window_size())            # {width: ,  height:}
print(driver.get_window_rect())             # {width: , height: , x: , y: }

print(driver.name)          # returns the name of the browser
print(driver.current_url)   # returns the url launched
print(driver.title)         # returns the title of the webpage

# close the session
driver.close()              # current active window

# driver.quit()             # close the entire session
