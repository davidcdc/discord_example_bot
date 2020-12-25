import discord
import pendulum
from discord_token import *

client = discord.Client()

now = pendulum.now()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello bot'):
        await message.channel.send('Hello user!')

    if message.content.startswith('$time'):
        await message.channel.send(now)

client.run(token)
