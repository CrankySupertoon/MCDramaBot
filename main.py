#***************************************************************************#
#                                                                           #
# MCDramaBot - A Discord Bot That Causes Drama                              #
# https://github.com/CrankySupertoon/MCDramaBot                             #
# Copyright (C) 22020 CrankySupertoon. All rights reserved.                 #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#

import discord
import random
import os
import requests
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(description = "MC DramaBot", command_prefix = "/")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='x is a mod by Vazkii...'))
    print("################################################################")
    print(f"  __  __  ____ ____                            ____        _   ")
    print(f" |  \/  |/ ___|  _ \ _ __ __ _ _ __ ___   __ _| __ )  ___ | |_ ")
    print(f" | |\/| | |   | | | | '__/ _` | '_ ` _ \ / _` |  _ \ / _ \| __|")
    print(f" | |  | | |___| |_| | | | (_| | | | | | | (_| | |_) | (_) | |_ ")
    print(f" |_|  |_|\____|____/|_|  \__,_|_| |_| |_|\__,_|____/ \___/ \__|")
    print("                                                                ")
    print("################################################################")
    print("                                                                ")
    print("Running as: " + bot.user.name)
    print(f'Using Client ID: #{bot.user.id}')
    print("Discord.py: " + discord.__version__)
    print("Created by Cranky Supertoon#7376")


@bot.group()
async def drama(ctx):
    drama = requests.get('https://mc-drama.herokuapp.com/raw')
    await ctx.send(drama.text)

keep_alive()
token = os.environ.get("TOKEN")
bot.run(token)