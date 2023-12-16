import discord
import discord
from discord.ext import commands
from typing import Literal
import datetime
from datetime import timedelta
import asyncio
from discord import app_commands
from discord.ext import commands, tasks
from datetime import datetime
import platform

class ping(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.launch_time = datetime.datetime.utcnow()
  
    @commands.hybrid_command(description="Check the bots latency & uptime")
    async def ping(self, ctx):
        server_name = ctx.guild.name
        server_icon = ctx.guild.icon
        discord_latency = self.client.latency * 1000
        discord_latency_message = f"**Latency:** {discord_latency:.0f}ms"
        embed = discord.Embed(title="<:Network:1185700803747516457> Network Information", description=f"{discord_latency_message}\n**Uptime:** <t:{int(self.client.launch_time.timestamp())}:R>", color=0x2b2d31)
        embed.set_author(name=server_name, icon_url=server_icon)
        embed.set_thumbnail(url=ctx.guild.icon)
        await ctx.send(embed=embed)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(ping(client))     
