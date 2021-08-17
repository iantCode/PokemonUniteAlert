from selenium import webdriver
from bs4 import BeautifulSoup
import time

def getTwitterJpn():
    try:
        URL = 'https://twitter.com/poke_unite_jp'
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
            jpnFile = open('twitterJpn.txt', 'r+', encoding="utf-8")
        except:
            jpnFile = open('twitterJpn.txt', 'w+', encoding="utf-8")
        if jpnFile.readline() != link:
            jpnFile.close()
            open('twitterJpn.txt', 'w', encoding="utf-8").close()
            jpnFile = open('twitterJpn.txt', 'w', encoding="utf-8")
            jpnFile.write(link)
            jpnFile.close()

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
    print(getTwitterJpn())