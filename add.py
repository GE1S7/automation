from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()
W2_SSID = os.getenv("s5id")
W2_PASS = os.getenv("new_wlan_pass")
NEW_ADMIN_PASS = os.getenv("new_pass")

driver = webdriver.Chrome()
driver.get("http://192.168.8.1/html/quicksetup.html")
time.sleep(0.2)
curr_url = driver.current_url
print(curr_url)
login_box = driver.find_element(By.CLASS_NAME, "input")
login_box.send_keys(NEW_ADMIN_PASS)
login_box.send_keys(Keys.RETURN)
time.sleep(0.2)
driver.get("http://192.168.8.1/html/wlanbasicsettings.html")
editw2 = driver.find_element(By.XPATH, '//*[@id="ssid_list"]/tbody/tr[4]/td[5]/span')
editw2.click()
time.sleep(23423222)
