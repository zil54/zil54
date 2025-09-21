import time
from splinter import Browser
import subprocess
import pyautogui
import time
import zipfile
import os
executable_path = {'executable_path':'C:\Program Files\Chrome Driver\chromedriver.exe'}
browser = Browser('chrome', **executable_path)

url = "https://theweekinchess.com/twic"
browser.visit(url)
time.sleep(7)

for i in range(1469,1477):
	browser.visit('https://www.theweekinchess.com/zips/twic'+str(i)+'c6.zip')
	time.sleep(7)




# Paths
downloaded_zip = r"C:\path\to\downloaded\file.zip"
extract_folder = r"C:\path\to\extracted"
exe_path = r"C:\path\to\your\program.exe"

# Unzip the file
with zipfile.ZipFile(downloaded_zip, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

# Get the first extracted file (modify logic if multiple files exist)
extracted_files = os.listdir(extract_folder)
if extracted_files:
    unzipped_file = os.path.join(extract_folder, extracted_files[0])
else:
    raise FileNotFoundError("No files extracted!")

# Start the .exe program
subprocess.Popen(exe_path)
time.sleep(5)  # Wait for the program to fully launch

# Simulate dragging and dropping the file
pyautogui.moveTo(100, 100)  # Adjust coordinates for file location
pyautogui.mouseDown()
time.sleep(1)
pyautogui.moveTo(500, 500)  # Adjust coordinates for target drop area
pyautogui.mouseUp()

print(f"File {unzipped_file} dropped successfully!")




