import discord
from discord.ext import commands
import random


intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)


class Qa(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('8ball is ready')


    @commands.command(aliases=['8ball'])
    async def _8ball(self,ctx,*,question):
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

    @_8ball.error
    async def error(self, ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("Digite uma pergunta após o comando")

def setup(client):
    client.add_cog(Qa(client))
    
