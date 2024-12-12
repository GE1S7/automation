from selenium import webdriver
# keyboard keys
from selenium.webdriver.common.keys import Keys
# locate elements within a document
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://192.168.8.1/html/quicksetup.html")
# is webpage title right?
# assert "Mobile Broadband" in driver.title
if "Mobile Broadband" in driver.title:
    print("I'm in.")


