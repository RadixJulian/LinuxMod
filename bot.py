import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands

load_dotenv()

TOKEN = os.getenv("DISCORD_API_TOKEN")

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is online!")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
    mod_logs = bot.get_channel(1172286709480828958)
    if reason == None:
        reason="No Reason Provided."
    await ctx.guild.kick(member)
    await ctx.send(f"User {member.mention} has been kicked for {reason}")

    embed = discord.Embed(title=":athletic_shoe: Kick Log", colour=discord.Colour.random())
    embed.set_author(name=f"{ctx.message.author.name}", icon_url=f"{ctx.message.author.display_avatar}")
    embed.add_field(name="Member ", value=f"{member.name}")
    embed.add_field(name="Reason ", value=f"{reason}")

    if not mod_logs:
        return 
    await mod_logs.send(embed=embed) ##f"User {member.mention} has been kicked for {reason} by {ctx.message.author.mention}")

bot.run(TOKEN)