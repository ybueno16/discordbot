from cmath import pi
import discord,os,sys
from discord.ext import commands
from icrawler.builtin import GoogleImageCrawler



caminho = "./img/"




class Image(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Image sender is ready")    

    
        
    @commands.command()
    async def image(self,ctx,question):

        
        google_Crawler = GoogleImageCrawler(storage = {'root_dir': caminho})
        google_Crawler.crawl(keyword = question, max_num = 1)
        await ctx.send(file = discord.File(caminho + "000001.jpg"))
        
        try:
            os.remove(caminho + "000001.jpg")
            print("depois remoção")
        except OSError as e:
            print(f"Error:{e.strerror}")

    


def setup(client):
    client.add_cog(Image(client))