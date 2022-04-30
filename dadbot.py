from discord.ext import commands
import discord
from discord import Webhook, RequestsWebhookAdapter

import aiohttp

import re
import random

bot = commands.Bot(command_prefix='!')

client = discord.Client()

#bot's token
TOKEN = 'x'

gen1_channel = 'channel_id'

expr = re.compile(r"I(?:'| a|*)m (.*)", re.IGNORECASE)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.id != message.author.id:
        if message.channel.id == gen1_channel:
            match = re.search(expr, message.content)
            choice = random.randint(0,1)
            name = message.author.display_name
            if match:
                resp = match.group(1)
                if choice == 0:
                    print(f"\t: Hi {resp}, I'm BOTNAME")
                    await message.channel.send(f"\tHi {resp}, I'm BOTNAME")
                elif choice == 1:
                    print(f"\t: You're not {resp}, you're {name}!")
                    await message.channel.send(f"\tYou're not {resp}, you're {name}!")
"""
#alternatively-
@client.event
async def on_message(message):
    await dadjoke(message)


async def dadjoke(message):
    if message.author.id != client.user.id and (message.channel.id == gen1_channel):
        word = re.search(r'\bi\'?m\s+(.*)', message.content, re.IGNORECASE)
        if word is not None:
            if len(word.group(1)) > 32:
                word = re.search(r'\bi\'?m\s+(\w+)', message.content, re.IGNORECASE)
            word = word.group(1)
            await message.channel.send('Hi {}, I\'m BOTNAME!'.format(word))
            if message.guild.me.guild_permissions.manage_nicknames and message.author.top_role < message.guild.me.top_role:
                if len(word) > 32:
                    word = word[:31]
                await message.author.edit(nick=word)
            else:
                await message.channel.send('Hey! Who stole my pencil! I can\'t nick anyone!')
"""   


client.run(TOKEN)
