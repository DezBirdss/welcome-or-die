import discord
import discord
from discord.ext import commands
from typing import Literal
import datetime
from datetime import timedelta
import asyncio
from discord import app_commands
from discord.ext import commands, tasks
import platform
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

URL = os.getenv('MONGO_URL')
load_dotenv()
client = AsyncIOMotorClient(URL)
db = client['WelcomeOrDie']
saves = db['Saves']

class savestats(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
  
    @commands.hybrid_group()
    async def saves(self, ctx):
        return
    

    @saves.command(description="View how someone has times saved someone")
    async def stats(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        savesresult = await saves.find_one({"_id": member.id})
        if savesresult == None:
            savess = 0
            emoji = "💀"
        else:
            savess = savesresult["saves"]    
            emoji = "🎉"

        await ctx.send(f"{emoji} **{member.display_name}** has saved `{savess}` people.")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(savestats(client))     
