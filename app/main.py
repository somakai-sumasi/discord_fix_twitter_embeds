import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from edit_url import edit_twitter_url, suppress_embeds

load_dotenv()
intents = discord.Intents.all()
activity = discord.Activity(name="MyBot", type=discord.ActivityType.custom)
bot = commands.Bot(
    command_prefix="!", intents=intents, activity=activity, help_command=None
)


# bot起動時
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


# メッセージ受信時のイベント
@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    parse_message = edit_twitter_url(message.content)
    if parse_message == "":
        return

    await message.channel.send(parse_message, silent=True)
    await suppress_embeds(message)


TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
