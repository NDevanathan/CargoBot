#CargoBot.py
"""
@author: Nikhil Devanathan
This script handles the functionality of CargoBot, a discord bot that can be used to populate servers from text files
and dump server structures to text files.
"""
#Default packages
import os
import csv
from collections import defaultdict

#Installed packages
import discord
import emoji
from dotenv import load_dotenv

#The bot secrets are stored in a local .env file for security. No peeking :)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

async def handle_help(message):
    i = 0

async def handle_dump_server(message):
    i = 0

async def handle_deploy_server(message):
    i = 0

async def handle_error(message):
    i = 0

FCTS_DICT = {'help':handle_help,
'dump':handle_dump_server,
'deploy':handle_deploy_server,
}

#Fires when the bot connects to a serevr it has joined. Exists as a dev-side tool.
@client.event
async def on_ready():
    for guild in client.guilds:
        print(f'{client.user} has connected to {guild.name}!')

#The bot always listens for messages, but it only responds when a message begins with !cargo
@client.event
async def on_message(message):
    if message.guild:                              #This bot is designed for server use only
        if ('!cargo' == message.content[:4].lower()):
            args = message.content.lower().split(' ')
            args[:] = [arg for arg in args if arg != '']
            if FCTS_DICT[args[1]]:
                await FCTS_DICT[args[1]](message)
            else:
                await handle_error(message)

#Runs the bot. Wouldn't want to forget this.
client.run(TOKEN)