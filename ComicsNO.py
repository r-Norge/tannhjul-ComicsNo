import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import aiohttp
from io import BytesIO
import random


class Dicks:

    def __init__(self):
        self.session = aiohttp.ClientSession(loop=self.loop)

    def randfunc(self):
        dab = Dagbladet()
        #ess = EnStripeSide()
        #tu = TekniskUkeblad()
        #bt = BergensTidene()
        functions = ['dagpondus', 'daglunch', "dagnemi"]
        rand = random.choice(functions)
        function=getattr(dab, rand)
        return function()

    async def temp(self, url):
        async with self.session.get(url) as resp:
            buffer = BytesIO(await resp.read())
            return buffer


class Dagbladet:
    page = requests.get('https://www.dagbladet.no/tegneserie')
    soup = BeautifulSoup(page.text, 'html.parser')
    frontpage = soup.find(class_='frontpage')
    frontpage_list = frontpage.find_all("article")

    def dagpondus(self):
        for article in Dagbladet.frontpage_list:
            title = article.find('h1').getText()
            if title == "Pondus":
                comic = article.find("img")['src']
                return comic

    def daglunch(self):
        for article in Dagbladet.frontpage_list:
            title = article.find('h1').getText()
            if title == "Lunch":
                comic = article.find("img")['src']
                return comic

    def dagnemi(self):
        for article in Dagbladet.frontpage_list:
            title = article.find('h1').getText()
            if title == "Nemi":
                comic = article.find("img")['src']
                return comic

    def daglille(self):
        for article in Dagbladet.frontpage_list:
            title = article.find('h1').getText()
            if title == "Lille Berlin":
                comic = article.find("img")['src']
                return comic

    def dagdunce(self):
        for article in Dagbladet.frontpage_list:
            title = article.find('h1').getText()
            if title == "Dunce":
                comic = article.find("img")['src']
                return comic

    def dagrocky(self):
        for article in Dagbladet.frontpage_list:
            title = article.find('h1').getText()
            if title == "Rocky":
                comic = article.find("img")['src']
                return comic

    def dagintet(self):
        for article in Dagbladet.frontpage_list:
            title = article.find('h1').getText()
            if title == "Intet nytt fra hjemmefronten":
                comic = article.find("img")['src']
                return comic

    def dagfagprat(self):
        for article in Dagbladet.frontpage_list:
            title = article.find('h1').getText()
            if title == "Fagprat":
                comic = article.find("img")['src']
                return comic

    def dagting(self):
        for article in Dagbladet.frontpage_list:
            title = article.find('h1').getText()
            if title == "Ting jeg gjorde":
                comic = article.find("img")['src']
                return comic

    def dagrutetid(self):
        for article in Dagbladet.frontpage_list:
            title = article.find('h1').getText()
            if title == "Rutetid":
                comic = article.find("img")['src']
                return comic

    def dagfirekanta(self):
        for article in Dagbladet.frontpage_list:
            title = article.find('h1').getText()
            if title == "Firekanta":
                comic = article.find("img")['src']
                return comic

    def dagpuma(self):
        for article in Dagbladet.frontpage_list:
            title = article.find('h1').getText()
            if title == "Puma":
                comic = article.find("img")['src']
                return comic


class BergensTidene:
    page = requests.get('https://www.bt.no/kultur/tegneserier/')
    soup = BeautifulSoup(page.text, 'html.parser')
    frontpage = soup.find(class_='cartoons')
    frontpage_list = frontpage.find_all("article")

    def dagpondus(self):
        for article in BergensTidene.frontpage_list:
            article = article.find(class_='cartoon-img-container')
            title = article.find('img')['alt']
            if title == "Pondus":
                comic = article.find("img")['src']
                return comic

    def dagnemi(self):
        for article in BergensTidene.frontpage_list:
            article = article.find(class_='cartoon-img-container')
            title = article.find('img')['alt']
            if title == "Nemi":
                comic = article.find("img")['src']
                return comic

    def daghjalmar(self):
        for article in BergensTidene.frontpage_list:
            h2 = article.find('h2')
            if h2 is not None:
                if h2.getText() == "Hjalmar":
                    comic = article.find("img")['src']
                    return comic


class TekniskUkeblad:
    def dagdilbert(self):
        page = requests.get('https://www.tu.no/tegneserier/dilbert')
        soup = BeautifulSoup(page.text, 'html.parser')
        frontpage = soup.find(class_='comic-view')
        sub = frontpage.find("img")['src']
        comic = "https://www.tu.no" + sub
        return comic

    def daglunch(self):
        page = requests.get('https://www.tu.no/tegneserier/lunch/')
        soup = BeautifulSoup(page.text, 'html.parser')
        frontpage = soup.find(class_='comic-view')
        sub = frontpage.find("img")['src']
        comic = "https://www.tu.no" + sub
        return comic


class Tek:
    def dagxkcd(self):
        page = requests.get('https://www.tek.no/tegneserier/1')
        soup = BeautifulSoup(page.text, 'html.parser')
        frontpage = soup.findAll(class_='comic-view')
        article = frontpage[3].find("noscript")
        comic = article.find("img")['src']
        return "https://www.tek.no" + comic

    def daggeek(self):
        page = requests.get('https://www.tek.no/tegneserier/6')
        soup = BeautifulSoup(page.text, 'html.parser')
        frontpage = soup.findAll(class_='comic-view')
        article = frontpage[19].find("noscript")
        comic = article.find("img")['src']
        return "https://www.tek.no" + comic

class EnStripeSide:
    def adressapondus(self):
        page = requests.get('https://www.adressa.no/kultur/tegneserier/')
        soup = BeautifulSoup(page.text, 'html.parser')
        frontpage = soup.find(class_='lp_pondusstripe')
        article = frontpage.find("figure")
        comic = article.find("img")['src']
        return comic


class ComicsNO:
    """Gets norwegian comics links from various news-outlets"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=bot.loop)

    @commands.group(name="db", pass_context=True, no_pm=True, invoke_without_command=True)
    async def db(self, ctx):
        """Gets random comics from Dagbladet"""
        rand = Dicks.randfunc(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, rand)
        await self.bot.send_cmd_help(ctx)
        await self.bot.send_message(ctx.message.channel, "You Failed, here is a random comic")
        await self.bot.send_file(channel, fp=buffer, filename="something.png")



    @db.command(name="pondus", pass_context=True, no_pm=True)
    async def dbpondus(self, ctx):
        """Gets Pondus from Dagbladet"""
        output = Dagbladet.dagpondus(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @db.command(name="lunch", pass_context=True, no_pm=True)
    async def dblunch(self, ctx):
        """Gets Lunch from Dagbladet"""
        output = Dagbladet.daglunch(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @db.command(name="nemi", pass_context=True, no_pm=True)
    async def dbnemi(self, ctx):
        """Gets Nemi from Dagbladet"""
        output = Dagbladet.dagnemi(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @db.command(name="dunce", pass_context=True, no_pm=True)
    async def dbdunce(self, ctx):
        """Gets Dunce from Dagbladet"""
        output = Dagbladet.dagdunce(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @db.command(name="rocky", pass_context=True, no_pm=True)
    async def dbrocky(self, ctx):
        """Gets Rocky from Dagbladet"""
        output = Dagbladet.dagrocky(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @db.command(name="intet", pass_context=True, no_pm=True)
    async def dbintet(self, ctx):
        """Gets Intet nytt fra hjemmefronten from Dagbladet"""
        output = Dagbladet.dagintet(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @db.command(name="fagprat", pass_context=True, no_pm=True)
    async def dbfagprat(self, ctx):
        """Gets Fagprat from Dagbladet"""
        output = Dagbladet.dagfagprat(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @db.command(name="ting", pass_context=True, no_pm=True)
    async def dbting(self, ctx):
        """Gets Ting jeg gjorde from Dagbladet"""
        output = Dagbladet.dagting(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @db.command(name="rutetid", pass_context=True, no_pm=True)
    async def dbrutetid(self, ctx):
        """Gets Rutetid from Dagbladet"""
        output = Dagbladet.dagrutetid(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @db.command(name="firekanta", pass_context=True, no_pm=True)
    async def dbfirekanta(self, ctx):
        """Gets Firekanta from Dagbladet"""
        output = Dagbladet.dagfirekanta(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @db.command(name="puma", pass_context=True, no_pm=True)
    async def dbpuma(self, ctx):
        """Gets Puma from Dagbladet"""
        output = Dagbladet.dagpuma(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @db.command(name="lille", pass_context=True, no_pm=True)
    async def dblille(self, ctx):
        """Gets Lille Berlin from Dagbladet"""
        output = Dagbladet.daglille(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")


    @commands.group(name="bt", pass_context=True, no_pm=True, invoke_without_command=True)
    async def bt(self, ctx):
        """Gets random comics from BergensTidene"""
        rand = Dicks.randfunc(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, rand)
        await self.bot.send_cmd_help(ctx)
        await self.bot.send_message(ctx.message.channel, "You Failed, here is a random comic")
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @bt.command(name="pondus", pass_context=True, no_pm=True)
    async def btpondus(self, ctx):
        """Gets Pondus from BergensTidene"""
        output = BergensTidene.dagpondus(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @bt.command(name="nemi", pass_context=True, no_pm=True)
    async def btnemi(self, ctx):
        """Gets Nemi from BergensTidene"""
        output = BergensTidene.dagnemi(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @bt.command(name="hjalmar", pass_context=True, no_pm=True)
    async def bthjalmar(self, ctx):
        """Gets Hjalmar from BergensTidene"""
        output = BergensTidene.dagnemi(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @commands.group(name="tu", pass_context=True, no_pm=True, invoke_without_command=True)
    async def tu(self, ctx):
        """Gets random comics from TU.no"""
        rand = Dicks.randfunc(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, rand)
        await self.bot.send_cmd_help(ctx)
        await self.bot.send_message(ctx.message.channel, "You Failed, here is a random comic")
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @tu.command(name="dilbert", pass_context=True, no_pm=True)
    async def tudilbert(self, ctx):
        """Gets Dilbert from TekniskUkeblad"""
        output = TekniskUkeblad.dagdilbert(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @tu.command(name="lunch", pass_context=True, no_pm=True)
    async def tulunch(self, ctx):
        """Gets Pondus from TekniskUkeblad"""
        output = TekniskUkeblad.daglunch(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")


    @commands.group(name="tek", pass_context=True, no_pm=True, invoke_without_command=True)
    async def tek(self, ctx):
        """Gets random comics from Tek.no"""
        rand = Dicks.randfunc(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, rand)
        await self.bot.send_cmd_help(ctx)
        await self.bot.send_message(ctx.message.channel, "You Failed, here is a random comic")
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @tek.command(name="xkcd", pass_context=True, no_pm=True)
    async def xkcd(self, ctx):
        """Gets XKCD from tek.no"""
        output = Tek.dagxkcd(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @tek.command(name="geek", pass_context=True, no_pm=True)
    async def geek(self, ctx):
        """Gets Geek And Poke from tek.no"""
        output = Tek.daggeek(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @commands.group(name="ess", pass_context=True, no_pm=True, invoke_without_command=True)
    async def ess(self, ctx):
        """Gets norwegian comics links from various news-outlets"""
        rand = Dicks.randfunc(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, rand)
        await self.bot.send_cmd_help(ctx)
        await self.bot.send_message(ctx.message.channel, "You Failed, here is a random comic")
        await self.bot.send_file(channel, fp=buffer, filename="something.png")

    @ess.command(name="pondus", pass_context=True, no_pm=True)
    async def adpondus(self, ctx):
        """Gets Pondus from Adressa"""
        output = EnStripeSide.adressapondus(self)
        channel = ctx.message.channel
        buffer = await Dicks.temp(self, output)
        await self.bot.send_file(channel, fp=buffer, filename="something.png")


def setup(bot):
    n = ComicsNO(bot)
    bot.add_cog(n)
