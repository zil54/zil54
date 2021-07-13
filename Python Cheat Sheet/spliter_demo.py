import time
from splinter import Browser
executable_path = {'executable_path':'C:\Program Files\Chrome Driver\chromedriver.exe'}
browser = Browser('chrome', **executable_path)

url = "https://theweekinchess.com/twic"
browser.visit(url)
time.sleep(7)

for i in range(1392,1393):
	browser.visit('https://www.theweekinchess.com/zips/twic'+str(i)+'c6.zip')
	time.sleep(7)


