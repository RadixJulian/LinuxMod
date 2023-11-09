import discord
import asyncio
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_API_TOKEN")

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="kkk.", intents=intents,  help_command=None)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
        
async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())