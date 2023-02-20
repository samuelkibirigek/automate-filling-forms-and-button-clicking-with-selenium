from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("C:/Users/Sam/Desktop/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Kalule")

l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Kibirige")

email = driver.find_element(By.NAME, "email")
email.send_keys("samuel@gmail.com")

send_button = driver.find_element(By.CLASS_NAME, "btn-block")
send_button.click()

driver.quit()

