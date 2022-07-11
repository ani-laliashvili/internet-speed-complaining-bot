from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

TWITTER_ID = 'MYTWITTEREMAILORPHONE'
PASSWORD = 'MYTWITTERPASSWORD'
CHROME_DRIVER_PATH = 'C:\\PATH\\chromedriver.exe'
PROVIDER_NAME = 'INTERNETPROVIDERTWITTERHANDLE'
USERNAME = 'TWITTERUSERNAME'

PROMISED_DOWN = 100
PROMISED_UP = 10

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
        time.sleep(5)
        self.driver.maximize_window()
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(5)

        button = self.driver.find_element(By.CSS_SELECTOR, '.start-button a')
        button.click()
        time.sleep(40)
        try:
            self.down = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
            self.up = float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)
        except:
            time.sleep(20)
            self.down = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
            self.up = float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            tweet = f'Hey @{PROVIDER_NAME}, why is my internet speed {self.down}down/{self.up}up ' \
                    f'when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?'

            self.driver.get('https://twitter.com/i/flow/login')
            time.sleep(5)

            self.driver.maximize_window()
            time.sleep(3)

            self.driver.find_element(By.NAME, 'text').send_keys(TWITTER_ID)
            time.sleep(3)

            self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
            time.sleep(3)

            try:
                self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(f'@{USERNAME}')
                self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
                time.sleep(3)
            except:
                print('')

            self.driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
            time.sleep(3)

            self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
            time.sleep(5)

            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div').click()
            time.sleep(2)

            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(tweet)
            time.sleep(3)

            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()

    def quit_driver(self):
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

bot.quit_driver()
