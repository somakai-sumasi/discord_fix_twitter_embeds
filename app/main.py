import math
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from edit_url import edit_twitter_url

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
    url = edit_twitter_url(message.content)
    if url == '':
        return None

    permissions = message.channel.permissions_for(message.guild.me)

    if not permissions.send_messages or not permissions.embed_links:
        return

    if permissions.manage_messages:
        try:
            await message.edit(suppress=True)
        except Exception as e:
            return

    await message.channel.send(url)


TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
