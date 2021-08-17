from selenium import webdriver
from bs4 import BeautifulSoup

def getYoutubeEng():
    URL = 'https://www.youtube.com/c/pokemonunite/videos'

    driver = webdriver.Edge(executable_path='D:\\Project\\uniteWebCrawler\\driver\\msedgedriver.exe')
    driver.get(url=URL)
    driver.implicitly_wait(time_to_wait=10)

    bs = BeautifulSoup(driver.page_source, 'lxml')
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
    getYoutubeEng()