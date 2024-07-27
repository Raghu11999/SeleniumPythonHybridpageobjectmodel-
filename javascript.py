import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo")
time.sleep(5)

driver.execute_script("alert('PYthon selenium')")
time.sleep(3)
driver.quit()