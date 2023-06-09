from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.maximize_window()
driver.get("https://app.jubelio.com/login")


driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
driver.find_element(By.NAME, "password").send_keys("invalidpassword")
driver.find_element(By.CLASS_NAME, "ladda-label").click()
time.sleep(3)
element = driver.find_element(By.XPATH, "//div[contains(@class, 'app-alert') and contains(@class, 'alert-danger')]")
print(element.is_enabled(), 'User received notification "Password atau email anda salah"')

driver.quit()