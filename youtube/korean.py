from selenium import webdriver
from bs4 import BeautifulSoup

def getYoutubeKor():
    URL = 'https://www.youtube.com/user/PokemonKoreaInc/videos'

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
        korFile = open('youtubeKor.txt', 'r+', encoding="utf-8")
    except:
        korFile = open('youtubeKor.txt', 'w+', encoding="utf-8")

    korTitle = korFile.readline()
    if 'Pokémon UNITE' in titles[0].text and korTitle != titles[0].text:
        korFile.close()
        open('youtubeKor.txt', 'w', encoding="utf-8").close()
        korFile = open('youtubeKor.txt', 'w', encoding="utf-8")
        korFile.write(titles[0].text)
        korFile.close()
        return titles[0].text, titles[0].attrs['href'], images[0].attrs['src']
    return '', '', ''

if __name__ == '__main__':
    getYoutubeKor()