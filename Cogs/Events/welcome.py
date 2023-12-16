import discord
import discord
from discord.ext import commands
from typing import Literal
import datetime
from datetime import timedelta
import asyncio
from discord import app_commands
from discord.ext import commands, tasks
import pytz
import platform
from dotenv import load_dotenv
import os




class welcomeevent(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):

        welcome_channel = member.guild.get_channel(1185596178155450541)
        print(welcome_channel)
        if welcome_channel:
            welcome_message = f'👋 Welcome {member.mention} to **{member.guild.name}**!\n<:ArrowDropDown:1185612975969677322> Please say **"welcome"** *to save this person life.* (They will be kicked in 30 seconds)'
            await welcome_channel.send(welcome_message)
            msg = await member.send(f"👋 **Welcome to the server, {member.mention}!** Brace yourself, though. 🚨 To survive, you must earn a welcome from a fellow member. Good luck! 🌟")
            await welcome_channel.set_permissions(member, send_messages=False)

            try:
                def check(message):
                    return (
                        message.content.lower() == "welcome" and
                        message.channel == welcome_channel and
                        message.author != self.client.user
                    )

                response = await self.client.wait_for('message', check=check, timeout=30)

                await welcome_channel.send(f"❤️ {member.mention} has been saved by **@{response.author.name}**")
                await welcome_channel.set_permissions(member, send_messages=True) 
                await msg.reply(f"❤️ **Congratulations, {member.display_name}**, you have survived! 🎉")

            except asyncio.TimeoutError:
                await welcome_channel.send(f"<:Dead:1185597929780678786> {member.mention} has died from no one welcoming them.")
                await member.kick(reason="No one welcomed them")
                await msg.reply(f"🫀 **I'm sorry, {member.mention}**, no one welcomed you. You have died. 💀")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(welcomeevent(client))     
