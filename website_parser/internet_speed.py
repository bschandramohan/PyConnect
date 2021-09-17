from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

chrome_driver_path="/Users/Chandra/Softwares/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.speedtest.net/")

# try:
#     # go_button_visible = WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.CLASS_NAME, "start-button")))
#     go_button_visible = WebDriverWait(driver, 300).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, "start-button")))
#
# except Exception as ex:
#     print("Go Button not visible")
# else:

start_button = driver.find_element_by_css_selector(".start-button a")
print(start_button.text)
start_button.click()
time(60)

try:
    result_present = WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.CLASS_NAME, "result-label")))
except Exception as ex:
    print("Result couldn't be found")
else:
    print("Download Speed", driver.find_element_by_class_name("download-speed"))
    print("Upload Speed", driver.find_element_by_class_name("upload-speed"))

driver.close()
