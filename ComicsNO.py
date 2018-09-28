import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import aiohttp
from io import BytesIO
import random


class Search:


    def dagbladet(self, querry):
        page = requests.get('https://www.dagbladet.no/tegneserie')
        soup = BeautifulSoup(page.text, 'html.parser')
        frontpage = soup.find(class_='frontpage')
        frontpage_list = frontpage.find_all("article")
        for article in frontpage_list:
            title = article.find('h1').getText()
            if title.lower() == querry.lower():
                comic = article.find("img")['src']
                return comic

    def bergenstidene(self, querry):
        page = requests.get('https://www.bt.no/kultur/tegneserier/')
        soup = BeautifulSoup(page.text, 'html.parser')
        frontpage = soup.find(class_='cartoons')
        frontpage_list = frontpage.find_all("article")

        for article in frontpage_list:
            article = article.find(class_='cartoon-img-container')
            title = article.find('img')['alt']
            if title.lower() == querry.lower():
                comic = article.find("img")['src']
                return comic


class ComicsNO:
    """Gets norwegian comics links from various news-outlets"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=bot.loop)

    async def temp(self, url):
        async with self.session.get(url) as resp:
            buffer = BytesIO(await resp.read())
            return buffer

    @commands.command(name="db", pass_context=True, no_pm=True, invoke_without_command=True)
    async def db(self, ctx, querry):
        """Gets Comics from Dagbladet"""
        get = Search.dagbladet(self, querry)

        if get is not None:
            channel = ctx.message.channel
            buffer = await ComicsNO.temp(self, get)
            await self.bot.send_file(channel, fp=buffer, filename="something.png")
        else:
            await self.bot.send_message(ctx.message.channel, "No results for {0}".format(querry))

    @commands.command(name="bt", pass_context=True, no_pm=True, invoke_without_command=True)
    async def bt(self, ctx, querry):
        """Gets Comics from BergensTidene"""
        get = Search.bergenstidene(self, querry)

        if get is not None:
            channel = ctx.message.channel
            buffer = await ComicsNO.temp(self, get)
            await self.bot.send_file(channel, fp=buffer, filename="something.png")
        else:
            await self.bot.send_message(ctx.message.channel, "No results for {0}".format(querry))



def setup(bot):
    n = ComicsNO(bot)
    bot.add_cog(n)
