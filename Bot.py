import discord
from discord.ext import commands
import random



intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents =discord.Intents.all())


@client.event
async def on_ready():
    print('bot is ready')


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server!')


@client.event
async def on_member_removed(member):
            print(f'{member} has lefted the server!')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')



@client.command(aliases=['8ball','teste'])
async def _8ball(ctx,*,question):
    responses = ["It is certain.",
                        "It is decidedly so.",
                        "Without a doubt.",
                        "Yes - definitely.",
                        "You may rely on it.",
                        "As I see it, yes.",
                        "Most likely.",
                        "Outlook good.",
                        "Yes.",
                        "Signs point to yes.",
                        "Reply hazy, try again.",
                        "Ask again later.",
                        "Better not tell you now.",
                        "Cannot predict now.",
                        "Concentrate and ask again.",
                        "Don't count on it.",
                        "My reply is no.",
                        "My sources say no.",
                        "Outlook not so good.",
                        "Very doubtful."
                    ]

    await ctx.send(f'Question:{question}\nAnswer:{random.choice(responses)}')



@commands.has_permissions(manage_messages = True)
@client.command()
async def clear(ctx, amount:int):
    await ctx.channel.purge (limit = amount + 1)


@client.command()
async def kick(ctx, member: discord.Member):



client.run('OTIwMDMzNzcxODQyMDU2MTkz.YbeeOA.cSgl1LnlB9ofLm3sILiBStCK2Uc')
