from twitter.japanese import getTwitterJpn
from twitter.english import getTwitterEng
from twitter.korean import getTwitterKor
from website.japanese import getWebsiteJpn
from website.english import getWebsiteEng
from website.korean import getWebsiteKor
from youtube.korean import getYoutubeKor
from youtube.japanese import getYoutubeJpn
from youtube.english import getYoutubeEng
from constants import TOKEN
import discord
import asyncio

client = discord.Client()

#TOKEN = 'YOUR TOKEN HERE'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

async def timer():
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(id=877109739182501902) # replace with channel_id
    while not client.is_closed():
        youtubeEngTitle, youtubeEngLink, youtubeEngImg = getYoutubeEng()
        if youtubeEngTitle != '':
            embed = discord.Embed(title="새 영어 유튜브 영상", description=youtubeEngTitle, url="https://youtube.com"+youtubeEngLink)
            embed.set_image(url=youtubeEngImg)
            await channel.send('@everyone', embed=embed)

        youtubeJpnTitle, youtubeJpnLink, youtubeJpnImg = getYoutubeJpn()
        if youtubeJpnTitle != '':
            embed = discord.Embed(title="새 일본어 유튜브 영상", description=youtubeJpnTitle, url="https://youtube.com"+youtubeJpnLink)
            embed.set_image(url=youtubeJpnImg)
            await channel.send('@everyone', embed=embed)

        youtubeKorTitle, youtubeKorLink, youtubeKorImg = getYoutubeKor()
        if youtubeKorTitle != '':
            embed = discord.Embed(title="새 한국어 유튜브 영상", description=youtubeKorTitle, url="https://youtube.com"+youtubeKorLink)
            embed.set_image(url=youtubeKorImg)
            await channel.send('@everyone', embed=embed)

        websiteKorTitle, websiteKorLink, websiteKorImg = getWebsiteKor()
        if websiteKorTitle != '':
            embed = discord.Embed(title="새 한국어 공식 사이트 공지", description=websiteKorTitle, url="https://pokemonkorea.co.kr"+websiteKorLink)
            embed.set_image(url=websiteKorImg)
            await channel.send('@everyone', embed=embed)

        websiteEngTitle, websiteEngLink, websiteEngImg = getWebsiteEng()
        if websiteEngTitle != '':
            embed = discord.Embed(title="새 영어 공식 사이트 공지", description=websiteEngTitle, url="https://unite.pokemon.com/en-us/news"+websiteEngLink)
            embed.set_image(url="https://unite.pokemon.com" + websiteEngImg)
            await channel.send('@everyone', embed=embed)

        websiteJpnTitle, websiteJpnLink, websiteJpnImg = getWebsiteJpn()
        if websiteJpnTitle != '':
            embed = discord.Embed(title="새 일본어 공식 사이트 공지", description=websiteJpnTitle, url="https://pokemonunite.jp"+websiteJpnLink)
            embed.set_image(url=websiteJpnImg)
            await channel.send('@everyone', embed=embed)

        twitterKorTitle, twitterKorLink= getTwitterKor()
        if twitterKorTitle != '':
            embed = discord.Embed(title="새 한국어 트위터 공지", description=twitterKorTitle, url="https://twitter.com"+twitterKorLink)
            await channel.send('@everyone', embed=embed)

        twitterEngTitle, twitterEngLink= getTwitterEng()
        if twitterEngTitle != '':
            embed = discord.Embed(title="새 영어 트위터 공지", description=twitterEngTitle, url="https://twitter.com"+twitterEngLink)
            await channel.send('@everyone', embed=embed)

        twitterJpnTitle, twitterJpnLink= getTwitterJpn()
        if twitterJpnTitle != '':
            embed = discord.Embed(title="새 일본어 트위터 공지", description=twitterJpnTitle, url="https://twitter.com"+twitterJpnLink)
            await channel.send('@everyone', embed=embed)

        await channel.send("Finished!")
        await asyncio.sleep(15)

if __name__ == '__main__':
    client.loop.create_task(timer())
    client.run(TOKEN)