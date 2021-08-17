from selenium import webdriver
from bs4 import BeautifulSoup

def getWebsiteKor():
    URL = 'https://www.pokemonkorea.co.kr/pokemon-unite/menu127'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
    driver.get(url=URL)
    driver.implicitly_wait(time_to_wait=10)

    bs = BeautifulSoup(driver.page_source, 'lxml')
    driver.close()
    titles = bs.select('.bx-txt > h3')
    images = bs.select('.tumb')

    try:
        korFile = open('websiteKor.txt', 'r+', encoding="utf-8")
    except:
        korFile = open('websiteKor.txt', 'w+', encoding="utf-8")
    if korFile.readline() != titles[0].text:
        korFile.close()
        open('websiteKor.txt', 'w', encoding="utf-8").close()
        korFile = open('websiteKor.txt', 'w', encoding="utf-8")
        korFile.write(titles[0].text)
        korFile.close()
        return titles[0].text, titles[0].parent.parent.attrs['href'], images[0].attrs['src']
    return '', '', ''

if __name__ == '__main__':
    print(getWebsiteKor())