# twitter-complaint-bot
Bot will check your internet speed automatically and will tweet to the service provider if the speed is less than promised speed.

## Prerequisites
* You need to have Python 3.7+ version installed.
* You need to have Selenium 4+ version installed, you can see my blog post on [How to set up the selenium for python development](https://medium.com/@gagandeepsingh2998/how-to-set-up-the-selenium-for-python-development-72c5e49341f9).

## Instructions
* Before using this project you need to make some changes.
* When you will see `main.py` first thing you need to change is `CHROME_DRIVER_PATH = "YOUR CHROME DRIVER'S PATH"`, you need to paste the path of chrome webdriver where it is in your local system.
  - If you don't have idea what is chrome webdriver's path, I highly recommend you to read this blog [How to set up the selenium for python development](https://medium.com/@gagandeepsingh2998/how-to-set-up-the-selenium-for-python-development-72c5e49341f9).
* Last two things you need to change `TWITTER_EMAIL = "YOUR TWITTER EMAIL"` put your twitter email inside the double quotes and `TWITTER_PASS = "YOUR TWITTER PASSWORD"` put your twitter password inside double quote.
* Now open the cmd and navigate to the project folder and hit `python main.py` or if you are using some ide just hit the run button.
