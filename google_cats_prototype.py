import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.google.com/")

driver.find_element(By.ID, "L2AGLb").click()
time.sleep(2)

googleSearchBox = driver.find_element(By.ID, "APjFqb")
googleSearchBox.send_keys("cats")
googleSearchBox.send_keys(Keys.RETURN)
driver.find_element(By.NAME, "btnK").click()
time.sleep(2)

driver.find_element(By.NAME, "btnK").click()
time.sleep(60)

driver.quit()

