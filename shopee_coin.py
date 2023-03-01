from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
user = config.get('info', 'account')
pwd = config.get('info', 'passwd')


driver = webdriver.Chrome()
driver.get(
    "https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2Fshopee-coins")

driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(pwd)

driver.find_element(By.CSS_SELECTOR, 'input[name="loginKey"]').send_keys(user)

time.sleep(0.5)
driver.find_elements(By.CSS_SELECTOR, 'button')[2].click()

try:
    driver.find_element(
        By.CSS_SELECTOR, 'button[class^="pcmall-dailycheckin"]').click()
except:
    driver.find_elements(By.CSS_SELECTOR, 'button')[2].click()

time.sleep(3)

try:
    verify_button = driver.find_element(
        By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[1]/div/div[2]/div/button')
    if(verify_button):
        verify_button.click()
except:
    print("don't need verify")

    # try:
    #     verifybutton = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[1]/div/div[2]/div/button')
    #     try:
    #         WebDriverWait(driver, 60).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[1]/div/div[2]/div/button'))
    #         )
    #         driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[1]/div/div[2]/div/button').click()
    #     except:
    #         print("dont need verify")

WebDriverWait(driver, 600).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "pcmall-dailycheckin_veN--o"))
)
time.sleep(3)
try:
    coinbutton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/main/section[1]/div[1]/div/section/div[2]/button')
    coinbutton.click()
except:
    print("error")
