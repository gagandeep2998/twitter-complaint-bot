from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "YOUR CHROME DRIVER'S PATH"
PROMISED_UP = 20
PROMISED_DOWN = 40
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASS = "YOUR TWITTER PASSWORD"
NET_SPEEED_URL = "https://www.speedtest.net/"
TWITTER_LOGIN_URL = "https://twitter.com/i/flow/login"


class InternetSpeedTwitterBot:
    """Class to represent internet speed Twitter bot."""
    def __init__(self) -> None:
        """Creates a new instance of service and chrome driver."""
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.up_speed = 0
        self.down_speed = 0

    def get_internet_speed(self) -> None:
        """Checks the internet speed of your connection.

        Calls the tweet_at_provider method if the speed is less than promised speed.
        """
        self.driver.get(NET_SPEEED_URL)
        test_button = self.driver.find_element(by=By.CLASS_NAME,
                                               value="js-start-test")
        time.sleep(5)
        test_button.click()
        time.sleep(60)
        up_speed_tag = self.driver.find_element(by=By.CLASS_NAME,
                                                value="upload-speed")
        down_speed_tag = self.driver.find_element(by=By.CLASS_NAME,
                                                  value="download-speed")
        self.up_speed = float(up_speed_tag.text)
        self.down_speed = float(down_speed_tag.text)
        print(self.up_speed)
        print(self.down_speed)
        if self.up_speed < PROMISED_UP or self.down_speed < PROMISED_DOWN:
            self.tweet_at_provider()

    def tweet_at_provider(self) -> None:
        """Logs in the Twitter and tweets about the low speed."""
        self.driver.get(TWITTER_LOGIN_URL)
        time.sleep(10)
        email_input = self.driver.find_element(by=By.CLASS_NAME,
                                               value="r-30o5oe")
        email_input.send_keys(TWITTER_EMAIL)
        time.sleep(5)
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)
        pass_input = self.driver.find_element(by=By.NAME,
                                              value="password")
        pass_input.send_keys(TWITTER_PASS)
        time.sleep(5)
        pass_input.send_keys(Keys.ENTER)
        time.sleep(20)

        tweet_input = self.driver.find_element(by=By.CLASS_NAME,
                                               value="public-DraftStyleDefault-block")
        my_tweet = f"My internet down speed {self.down_speed}, up speed {self.up_speed} what a slow net"
        tweet_input.send_keys(my_tweet)

        time.sleep(5)
        tweet_button = self.driver.find_element(by=By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                      'div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/'
                                                      'div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()

        time.sleep(30)

        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
