import datetime
import os
from logger_util2 import SeleniumExecutionLogger
from selenium import webdriver


#define logging and driver locations
logging_timestamp = (str(datetime.datetime.now().strftime("_%y_%m_%d_%H_%M_%S")))
currentDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(currentDir, 'webdrivers_repo/chromedriver.exe')

loggerObject = SeleniumExecutionLogger(currentDir)
driver = webdriver.Chrome(filename)

#value_true if <test> else value_false
#actual selenium run:
driver.get("https://www.python.org")
if driver.title is not None:
    loggerObject.log_success(driver.title, "test212", logging_timestamp + "_run1.txt")
else:
    loggerObject.log_failure("Failed to find the title of the expected page", "test212", logging_timestamp + "_run1.txt")






