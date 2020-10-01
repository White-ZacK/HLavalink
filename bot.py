import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix=">")

@bot.event
async def on_ready():
  print(f'{bot.user} has logged in.')
  bot.load_extension('cogs.WVL')

bot.run("NzYwMDg2MzM0MDY0MDMzNzky.X3G7jw.Pj18QeN9jFwfgjfkkuTSx8LHlkU")