from selenium import webdriver
from bs4 import BeautifulSoup

def getYoutubeJpn():
    URL = 'https://www.youtube.com/channel/UCvo8JUqHh2d1QGnK3LKyI4Q/videos'

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
        jpnFile = open('youtubeJpn.txt', 'r+', encoding="utf-8")
    except:
        jpnFile = open('youtubeJpn.txt', 'w+', encoding="utf-8")
    if jpnFile.readline() != titles[0].text:
        jpnFile.close()
        open('youtubeJpn.txt', 'w', encoding="utf-8").close()
        jpnFile = open('youtubeJpn.txt', 'w', encoding="utf-8")
        jpnFile.write(titles[0].text)
        jpnFile.close()
        return titles[0].text, titles[0].attrs['href'], images[0].attrs['src']
    return '', '', ''

if __name__ == '__main__':
    getYoutubeJpn()