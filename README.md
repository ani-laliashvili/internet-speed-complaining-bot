# Internet Speed Complaining Bot
This script uses Selenium to check internet upload and download speeds using https://www.speedtest.net/ and tweets to internet provider with details if speed is lower than expected.

## User Input
- TWITTER_ID : Email or phone number used for Twitter
- PASSWORD : Twitter password
- CHROME_DRIVER_PATH : The path of chromedriver.exe downloaded from https://chromedriver.chromium.org/downloads
- PROVIDER_NAME : Twitter handle of the internet provider
- USERNAME : Twitter user handle

- PROMISED_DOWN : Download speed promised per internet service provider
- PROMISED_UP : Upload speed promised per internet service provider

## Requirements
- Selenium
