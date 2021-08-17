from selenium import webdriver
from bs4 import BeautifulSoup
import time

def getTwitterEng():
    try:
        URL = 'https://twitter.com/PokemonUnite'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
        driver.get(url=URL)
        driver.implicitly_wait(time_to_wait=10)
        time.sleep(4)

        bs = BeautifulSoup(driver.page_source, 'lxml')
        driver.close()
        link = bs.select('[data-testid=\"tweet\"] > div > div > div > div > div > a')[1].attrs['href']

        try:
            engFile = open('twitterEng.txt', 'r+', encoding="utf-8")
        except:
            engFile = open('twitterEng.txt', 'w+', encoding="utf-8")
        if engFile.readline() != link:
            engFile.close()
            open('twitterEng.txt', 'w', encoding="utf-8").close()
            engFile = open('twitterEng.txt', 'w', encoding="utf-8")
            engFile.write(link)
            engFile.close()

            driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
            driver.get(url='https://twitter.com'+link)
            driver.implicitly_wait(time_to_wait=10)
            time.sleep(4)

            bs = BeautifulSoup(driver.page_source, 'lxml')
            driver.close()
            title = bs.select('[property=\"og:description\"]')[0].attrs['content']
            return title, link
        return '', ''
    except:
        return '', ''

if __name__ == '__main__':
    print(getTwitterEng())