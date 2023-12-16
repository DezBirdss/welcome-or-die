import discord
import platform
import sys
import discord.ext
from discord.ext import commands
from urllib.parse import quote_plus
from discord import app_commands
import discord
import datetime
from discord.ext import commands, tasks

from typing import Optional
import os
from dotenv import load_dotenv
from jishaku import Jishaku
import jishaku

import time
load_dotenv()
PREFIX = os.getenv('PREFIX')
TOKEN = os.getenv('TOKEN')
STATUS = os.getenv('STATUS')











class client(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix=commands.when_mentioned_or(PREFIX), intents=intents)
        self.client = client
        self.cogslist = ["Cogs.Events.welcome", "Cogs.Commands.Utilties.botinfo", "Cogs.Commands.Utilties.ping"]

    async def load_jishaku(self):
        await self.wait_until_ready()
        await self.load_extension('jishaku')        

    async def setup_hook(self):
        self.loop.create_task(self.load_jishaku()) 

        for ext in self.cogslist:
            await self.load_extension(ext)
            print(f"{ext} loaded")


    async def on_ready(self):
        prfx = (time.strftime("%H:%M:%S GMT", time.gmtime()))
        print(prfx + " Logged in as " + self.user.name)
        print(prfx + " Bot ID " + str(self.user.id))
        print(prfx + " Discord Version " +  discord.__version__)
        print(prfx + " Python Version " + str(platform.python_version()))
        synced = await self.tree.sync()
        print(prfx + " Slash CMDs Synced " + str(len(synced)) + " Commands")
        print(prfx + " Bot is in " + str(len(self.guilds)) + " servers")
 
    async def on_connect(self):
        activity2 = discord.CustomActivity(name=STATUS)

        print("Connected to Discord Gateway!")
        await self.change_presence(activity=activity2)

    async def on_disconnect(self):
        print("Disconnected from Discord Gateway!")

client = client()
client.run(TOKEN)    