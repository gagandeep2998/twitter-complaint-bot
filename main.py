from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
PROMISED_UP = 40
PROMISED_DOWN = 20
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASS = "YOUR TWITTER PASSWORD"
NET_SPEEED_URL = "https://www.speedtest.net/"
TWITTER_LOGIN_URL = "https://twitter.com/i/flow/login"


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

    def tweet_at_provider(self):
        self.driver.get(TWITTER_LOGIN_URL)
        time.sleep(10)
        email_input = self.driver.find_element(by=By.CLASS_NAME, value="r-30o5oe")
        email_input.send_keys(TWITTER_EMAIL)
        time.sleep(5)
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)
        pass_input = self.driver.find_element(by=By.NAME, value="password")
        pass_input.send_keys(TWITTER_PASS)
        time.sleep(5)
        pass_input.send_keys(Keys.ENTER)
        time.sleep(20)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
