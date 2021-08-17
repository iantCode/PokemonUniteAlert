from selenium import webdriver
from bs4 import BeautifulSoup

def getWebsiteEng():
    URL = 'https://unite.pokemon.com/en-us/news/'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
    driver.get(url=URL)
    driver.implicitly_wait(time_to_wait=10)

    bs = BeautifulSoup(driver.page_source, 'lxml')
    driver.close()
    title = bs.select('h2.vp-slide')[0].text
    image = bs.select('img.news-image')[0].attrs['src'].replace('../..', '')
    link = bs.select('a.button--pokeball')[0].attrs['href'].replace('./', '/')

    try:
        engFile = open('websiteEng.txt', 'r+', encoding="utf-8")
    except:
        engFile = open('websiteEng.txt', 'w+', encoding="utf-8")
    if engFile.readline() != title:
        engFile.close()
        open('websiteEng.txt', 'w', encoding="utf-8").close()
        engFile = open('websiteEng.txt', 'w', encoding="utf-8")
        engFile.write(title)
        engFile.close()
        return title, link, image
    return '', '', ''

if __name__ == '__main__':
    print(getWebsiteEng())