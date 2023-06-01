import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import pandas as pd
import numpy as np
from discord.ext import commands
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Setting up the Discord bot client with necessary intents
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # List of words to check in the message content
    words = ["charlène", "charlene"]
    # Convert the message content to lowercase for case-insensitive comparison
    content = message.content.lower()
    # Check if any of the words are present in the content
    should_react = any(word in content for word in words)
    if should_react:
        # React to the message with a crown emoji
        emoji = "👑"
        await message.add_reaction(emoji)

    await bot.process_commands(message)

@bot.command()
async def pred_nlp(context, message):
    # Remove the "!pred" prefix
    req = requests.get(f'https://appfake.azurewebsites.net/pred?text={message}').json()[0]
    if req == "1" :
        await context.send("This is FakeNews")
        await context.send("https://tenor.com/view/donald-trump-fake-news-gif-11382583")
    if req == "0" :
        await context.send("This is Real, but still be careful love !")
        await context.send("https://tenor.com/fr/view/pepo-gif-20505055")
# Run the bot using your Discord bot token

bot.run(TOKEN)

client.run(TOKEN)
