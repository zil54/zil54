import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


currentDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(currentDir,'webdrivers_repo/chromedriver.exe')
driver = webdriver.Chrome(filename)
driver.get("https://www.python.org")
print(driver.title)





