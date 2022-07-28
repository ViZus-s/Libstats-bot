import os
from dateutil import parser
from typing import Dict, Tuple, Union
import aiohttp
from disnake.utils import format_dt

LINKS: Dict[str, Tuple[str, ...]] = {
    "disnake": (
        "https://api.github.com/repos/DisnakeDev/disnake",
        "https://api.github.com/repos/DisnakeDev/disnake/commits",
        "https://api.github.com/search/issues?q=repo:disnakedev/disnake+type:issue+state:open",
        "https://api.github.com/repos/DisnakeDev/disnake/pulls",
    ),
    "nextcord": (
        "https://api.github.com/repos/nextcord/nextcord",
        "https://api.github.com/repos/nextcord/nextcord/commits",
        "https://api.github.com/search/issues?q=repo:nextcord/nextcord+type:issue+state:open",
        "https://api.github.com/repos/nextcord/nextcord/pulls",
    ),
    "pycord": (
        "https://api.github.com/repos/Pycord-Development/pycord",
        "https://api.github.com/repos/Pycord-Development/pycord/commits",
        "https://api.github.com/search/issues?q=repo:pycord-development/pycord+type:issue+state:open",
        "https://api.github.com/repos/Pycord-Development/pycord/pulls",
    ),
    "discord.py": (
        "https://api.github.com/repos/Rapptz/discord.py",
        "https://api.github.com/repos/Rapptz/discord.py/commits",
        "https://api.github.com/search/issues?q=repo:rapptz/discord.py+type:issue+state:open",
        "https://api.github.com/repos/Rapptz/discord.py/pulls",
    ),
    "interactions.py": (
        "https://api.github.com/repos/interactions-py/library",
        "https://api.github.com/repos/interactions-py/library/commits",
        "https://api.github.com/search/issues?q=repo:interactions-py/library+type:issue+state:open",
        "https://api.github.com/repos/interactions-py/library/pulls",
    ),
    "hikari": (
        "https://api.github.com/repos/hikari-py/hikari",
        "https://api.github.com/repos/hikari-py/hikari/commits",
        "https://api.github.com/search/issues?q=repo:hikari-py/hikari+type:issue+state:open",
        "https://api.github.com/repos/hikari-py/hikari/pulls",
    ),
}


async def parsing_git(library: str) -> Dict[str, Union[str, int]]:
    async with aiohttp.ClientSession(
        headers={"Authorization": f"token {os.environ.get('TOKEN')}"}
    ) as session:

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

    raw_last_commit = data2[0]["commit"]["committer"]["date"]
    last_commit = format_dt(parser.parse(raw_last_commit), "R")

    return {
        "stars": stars,
        "forks": forks,
        "issues": issues,
        "watching": watching,
        "pull requests": pull_requests,
        "last commit": last_commit,
    }


async def parsing_update() -> str:
    async with aiohttp.request(
        "GET", "https://api.github.com/repos/ViZus-s/Libstats-bot/commits"
    ) as response:
        data = await response.json()
    update = data[1]["commit"]["message"]
    return update
