import re
from urllib.parse import urlparse


def edit_twitter_url(txt: str):
    result = ""
    for match in re.finditer(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", txt):
        url = match.group()
        parse = urlparse(url)

        domain = parse.netloc
        if domain != "twitter.com" and domain != "x.com":
            continue

        convert_parse = parse._replace(netloc="vxtwitter.com")
        result += convert_parse.geturl() + "\n"

    return result
