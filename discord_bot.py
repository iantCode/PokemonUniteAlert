from youtube.korean import getYoutubeKor
from youtube.japanese import getYoutubeJpn
from youtube.english import getYoutubeEng
#import constants
import discord
import asyncio

client = discord.Client()

TOKEN = 'YOUR TOKEN HERE'

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

        await asyncio.sleep(15)

if __name__ == '__main__':
    client.loop.create_task(timer())
    client.run(TOKEN)