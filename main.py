from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
PROMISED_UP = 40
PROMISED_DOWN = 20
TWITTER_EMAIL = ""
TWITTER_PASS = ""
NET_SPEEED_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.up_speed = 0
        self.down_speed = 0

    def get_internet_speed(self):
        self.driver.get(NET_SPEEED_URL)
        test_button = self.driver.find_element(by=By.CLASS_NAME, value="js-start-test")
        time.sleep(5)
        test_button.click()
        time.sleep(60)
        self.up_speed = float(self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text)
        self.down_speed = float(self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text)
        print(self.up_speed)
        print(self.down_speed)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
