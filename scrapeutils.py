from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

class Scraper:
    def __init__(self):
        DRIVER_PATH = Service('driver/chromedriver')
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        self.driver = webdriver.Chrome(options=options, service=DRIVER_PATH)
        self.twitterUrl = "https://twitter.com/"
        self.allTweets = []

    def openTwitterProfile(self, handle):
        self.driver.get(f"https://twitter.com/{handle}")
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-testid="tweet"]')))

    def scrollToBottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(8)

    def getTweets(self, file, progress, task):
        for loop in range(5):      
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(8)

            for tweet in self.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]'):
                if not tweet.find_elements(By.CSS_SELECTOR, '[data-testid="videoPlayer"]') == []:
                    continue
                if not tweet.find_elements(By.CSS_SELECTOR, '[data-testid="card.wrapper"]') == []:
                    continue    
                post = tweet.find_elements(By.CSS_SELECTOR, '[data-testid="tweetText"]')
                if not post == []:
                    if post[0].text not in self.allTweets:
                        self.allTweets.append(post[0].text)
                        file.write(f"{post[0].text}\n##\n")
            self.scrollToBottom()
            progress.update(task, advance=1)

    def report(self):
        print(f"{len(self.allTweets)} tweets scrapped")
        self.driver.quit()