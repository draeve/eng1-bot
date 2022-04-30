from discord.ext import commands
import discord
from discord import Webhook, RequestsWebhookAdapter

import aiohttp

import os

bot = commands.Bot(command_prefix='!')

client = discord.Client()

#BOT TOKEN:
TOKEN = 'x'

channel_id = 0
user_id = 0
emote = 'emote'

async def get_emoji(guild: discord.Guild, arg):
    return get(ctx.guild.emojis, name=arg)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if client.user.id != message.author.id:

        if (message.author.id == user_id):
            #channel specific webhook
            webhook = Webhook.from_url("webhook link", adapter=RequestsWebhookAdapter())

            #auto adds reaction if the message is from a certain user
            await message.add_reaction(froge_emote)

            #auto responds to that user's message
            mention = message.author.mention
            response = f"{mention} Hello World!"

            webhook = await message.channel.create_webhook(name=message.author.name)
            await webhook.send(response)
    
client.run(TOKEN)



