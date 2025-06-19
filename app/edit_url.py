import asyncio
import re
from urllib.parse import urlparse

import discord


def edit_twitter_url(txt: str):
    result = ""

    spoiler_split = re.split(r"(\|\|.*?\|\|)", txt)

    for segment in spoiler_split:
        if segment.startswith("||") and segment.endswith("||"):
            result += replace_twitter_urls(segment, True)
        else:
            result += replace_twitter_urls(segment, False)

    return result


def replace_twitter_urls(txt: str, has_spoiler: bool = False):
    result = ""
    for match in re.finditer(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", txt):
        url = match.group()
        parse = urlparse(url)

        domain = parse.netloc
        if domain != "twitter.com" and domain != "x.com":
            continue

        convert_parse = parse._replace(netloc="fxtwitter.com")
        result += "[Tweetへ](" + convert_parse.geturl() + ")"
        if has_spoiler:
            result = "||" + result + "||"

        result += "\n"

    return result


async def suppress_embeds(message: discord.Message):
    await asyncio.sleep(0.1)

    permissions = message.channel.permissions_for(message.guild.me)

    if not permissions.send_messages or not permissions.embed_links:
        return
    if permissions.manage_messages:
        try:
            await message.edit(suppress=True)
        except Exception:
            return
