from selenium import webdriver
from bs4 import BeautifulSoup
import os

def getYoutubeEng():
    URL = 'https://www.youtube.com/c/pokemonunite/videos'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
    driver.get(url=URL)
    driver.implicitly_wait(time_to_wait=10)

    bs = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()
    titles = bs.select('#video-title')

    images = bs.select('#img')
    while 'ytimg' not in images[0].attrs['src']:
        del images[0]

    try:
        engFile = open('youtubeEng.txt', 'r+', encoding="utf-8")
    except:
        engFile = open('youtubeEng.txt', 'w+', encoding="utf-8")
    if engFile.readline() != titles[0].text:
        engFile.close()
        open('youtubeEng.txt', 'w', encoding="utf-8").close()
        engFile = open('youtubeEng.txt', 'w', encoding="utf-8")
        engFile.write(titles[0].text)
        engFile.close()
        return titles[0].text, titles[0].attrs['href'], images[0].attrs['src']
    return '', '', ''

if __name__ == '__main__':
    print(getYoutubeEng())