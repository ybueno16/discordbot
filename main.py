import discord
from discord.ext import commands,tasks
from itertools import cycle
import os


status = cycle(['Programando um bot para outro bot','Muitos jogos',';-;'])
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents =discord.Intents.all())


@client.event
async def on_ready():
    print('bot is ready')
    change_status.start()
    
    #Comando para deixar fixo uma status no discord
    
    #await client.change_presence(status = discord.Status.online,activity = discord.Game('Programando um bot para outro bot'))
    


#comando para troca de status discord
@tasks.loop(minutes=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))




#Tratamento de erros caso seja digitado algum comando inexistente
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("Comando inválido")




#Comandos para inicialização do cog

@client.command()
async def load(ctx,extension):
    client.load_extension(f'maincog.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'maincog.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')




client.run('OTIwMDMzNzcxODQyMDU2MTkz.YbeeOA.cSgl1LnlB9ofLm3sILiBStCK2Uc')
