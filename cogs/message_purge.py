import discord 
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

#Comando para apagar mensagens de um canal do discord

class Message_purge(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Message purge is ready")

        

    @commands.command(name='adm')
    @commands.has_permissions(manage_messages=True)
    async def adm(ctx:commands.Context):
       ctx.send('deu bom')
    
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self,ctx,amount:int):
         await ctx.channel.purge(limit = amount + 1)



    @clear.error
    async def clear_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("Digite o número desejado de mensagens a ser apagadas")


def setup(client):
    client.add_cog(Message_purge(client))
    