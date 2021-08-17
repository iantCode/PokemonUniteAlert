from selenium import webdriver
from bs4 import BeautifulSoup

def getWebsiteJpn():
    URL = 'https://www.pokemonunite.jp/ja/news/'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
    driver.get(url=URL)
    driver.implicitly_wait(time_to_wait=10)

    bs = BeautifulSoup(driver.page_source, 'lxml')
    driver.close()
    title = bs.select('.topics-header-heading')[0].text
    link = bs.select('a.topics-box')[0].attrs['href']
    image = bs.select('.ojf-img')[0].attrs['src']
    print(image)

    try:
        jpnFile = open('websiteJpn.txt', 'r+', encoding="utf-8")
    except:
        jpnFile = open('websiteJpn.txt', 'w+', encoding="utf-8")
    if jpnFile.readline() != title:
        jpnFile.close()
        open('websiteJpn.txt', 'w', encoding="utf-8").close()
        jpnFile = open('websiteJpn.txt', 'w', encoding="utf-8")
        jpnFile.write(title)
        jpnFile.close()
        return title, link, image
    return '', '', ''

if __name__ == '__main__':
    print(getWebsiteJpn())