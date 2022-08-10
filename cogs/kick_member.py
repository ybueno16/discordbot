
import discord
from discord.ext import commands


intents = discord.Intents(messages=True, guilds=True,
                          reactions=True, members=True, presences=True)


class Kick_member(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Kick member is ready")


    @commands.command
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)



    

def setup(client):
    client.add_cog(Kick_member(client))