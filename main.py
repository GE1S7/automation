from selenium import webdriver
# keyboard keys
from selenium.webdriver.common.keys import Keys
# locate elements within a document
from selenium.webdriver.common.by import By
# sleep
import time
# access to environmental variables
import os
from dotenv import load_dotenv

load_dotenv()
ADMIN_PASS=os.getenv("dft_pass")


driver = webdriver.Chrome()
driver.get("http://192.168.8.1/html/quicksetup.html")
# is webpage title right?
# assert "Mobile Broadband" in driver.title
if "Mobile Broadband" in driver.title:
    print("I'm in.")

login_box = driver.find_element(By.CLASS_NAME, "input")
login_box.clear()
#login_box.click()
login_box.send_keys(ADMIN_PASS)
login_box.send_keys(Keys.RETURN)
time.sleep(0.2)

au_box = driver.find_element(By.ID, "auto_update")
au_box.click()

next1 = driver.find_element(By.CLASS_NAME, "button_wrapper")
next1.click()

set_ssid = driver.find_element(By.ID, ssid_wifiName)
set_ssid.send_keys(new_ssid)




time.sleep(29999999)


#<input type="password" autocomplete="off" class="input" id="password" maxlength="32" tabindex="1" style="" data-protonpass-base-css="{&quot;padding-right&quot;:&quot;&quot;}">
