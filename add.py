from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import os
from dotenv import load_dotenv

load_dotenv()
NEW_ADMIN_PASS = os.getenv("new_pass") 
W2_SSID = os.getenv("s5id")
W2_PASS = os.getenv("new_wlan_pass")
ENCR_TYPE = os.getenv("encr_prot")

driver = webdriver.Chrome()
driver.get("http://192.168.8.1/html/quicksetup.html")
time.sleep(0.2)

login_box = driver.find_element(By.CLASS_NAME, "input")
login_box.send_keys(NEW_ADMIN_PASS)
login_box.send_keys(Keys.RETURN)
time.sleep(0.2)

driver.get("http://192.168.8.1/html/wlanbasicsettings.html")
editw2 = driver.find_element(By.XPATH, '//*[@id="ssid_list"]/tbody/tr[4]/td[5]/span')
editw2.click()

w2_ssid_name = driver.find_element(By.ID, "ssid_wifiName")
w2_ssid_name.clear()
w2_ssid_name.send_keys(W2_SSID)

select_element = driver.find_element(By.ID, "ssid_authentication")
select = Select(select_element)
selected_option_list = select.all_selected_options
time.sleep(0.2)
print(select.options)
select.select_by_value(ENCR_TYPE)

w2_key = driver.find_element(By.ID, "ssid_wpa_key")
w2_key.clear()
w2_key.send_keys(W2_PASS)

apply_btn = driver.find_element(By.ID, "apply_button")
apply_btn.click()

time.sleep(234234)
                                


