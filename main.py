import discord
import os

from discord.ext import commands

BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
intents = discord.Intents.all()

# Create a bot instance
bot = commands.Bot(command_prefix='!', intents=intents)


# Define a command
@bot.command()
async def hello(ctx):
    """A simple command that says hello"""
    await ctx.send('Hello!')

# Event to print bot's username and id when it's ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

# Run the bot with your token
bot.run(BOT_TOKEN)
