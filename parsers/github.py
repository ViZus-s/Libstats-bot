import os
import json
import time

import aiohttp
from bs4 import BeautifulSoup

LINKS = {"disnake": ("https://api.github.com/repos/DisnakeDev/disnake",
                     "https://api.github.com/repos/DisnakeDev/disnake/commits",
                     "https://api.github.com/search/issues?q=repo:disnakedev/disnake+type:issue+state:open",
                     "https://api.github.com/repos/DisnakeDev/disnake/pulls",),

         "nextcord": ("https://api.github.com/repos/nextcord/nextcord",
                      "https://api.github.com/repos/nextcord/nextcord/commits",
                      "https://api.github.com/search/issues?q=repo:nextcord/nextcord+type:issue+state:open",
                      "https://api.github.com/repos/nextcord/nextcord/pulls",),

         "pycord": ("https://api.github.com/repos/Pycord-Development/pycord",
                    "https://api.github.com/repos/Pycord-Development/pycord/commits",
                    "https://api.github.com/search/issues?q=repo:pycord-development/pycord+type:issue+state:open",
                    "https://api.github.com/repos/Pycord-Development/pycord/pulls",),

         "discord.py": ("https://api.github.com/repos/Rapptz/discord.py",
                        "https://api.github.com/repos/Rapptz/discord.py/commits",
                        "https://api.github.com/search/issues?q=repo:rapptz/discord.py+type:issue+state:open",
                        "https://api.github.com/repos/Rapptz/discord.py/pulls"),

         "interactions.py": ("https://api.github.com/repos/interactions-py/library",
                             "https://api.github.com/repos/interactions-py/library/commits",
                             "https://api.github.com/search/issues?q=repo:interactions-py/library+type:issue+state:open",
                             "https://api.github.com/repos/interactions-py/library/pulls"), }


async def parsing_git(library: str) -> dict:
    async with aiohttp.ClientSession(headers={"Authorization": f"token {os.environ.get('TOKEN')}"}) as session:

        async with session.get(LINKS[library][0]) as request:
            data = await request.json()  # stars, forks, watching

        async with session.get(LINKS[library][1]) as request:
            data2 = await request.json()  # commit

        async with session.get(LINKS[library][2]) as request:
            data3 = await request.json()  # issues

        async with session.get(LINKS[library][3]) as request:
            data4 = await request.json()  # pull_requests

    stars = data["stargazers_count"]
    forks = data["forks_count"]
    issues = data3["total_count"]
    watching = data["subscribers_count"]
    pull_requests = len(data4)

    last_commit = data2[0]["commit"]["committer"]["date"].replace("T", " ")[:-1]
    last_commit = f"<t:{int(time.mktime(time.strptime(last_commit, '%Y-%m-%d %H:%M:%S')))}>"

    return {"stars": stars,
            "forks": forks,
            "issues": issues,
            "watching": watching,
            "pull requests": pull_requests,
            "last commit": last_commit, }


async def parsing_update() -> str:
    async with aiohttp.request("GET", "https://api.github.com/repos/ViZus-s/Libstats-bot/commits") as response:
        result = await response.text()
        result = json.loads(result)
        return result[1]['commit']['message']
