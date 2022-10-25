import asyncio
import json
import time
from datetime import date, timedelta
from typing import Dict, Tuple, Union

import aiohttp
from bs4 import BeautifulSoup


LINKS: Dict[str, Tuple[str, str]] = {
    "disnake": (
        "https://pypistats.org/packages/disnake",
        "https://api.pepy.tech/api/v2/projects/disnake",
    ),
    "nextcord": (
        "https://pypistats.org/packages/nextcord",
        "https://api.pepy.tech/api/v2/projects/nextcord",
    ),
    "pycord": (
        "https://pypistats.org/packages/py-cord",
        "https://api.pepy.tech/api/v2/projects/py-cord",
    ),
    "discord.py": (
        "https://pypistats.org/packages/discord.py",
        "https://api.pepy.tech/api/v2/projects/discord.py",
    ),
    "interactions.py": (
        "https://pypistats.org/packages/discord-py-interactions",
        "https://api.pepy.tech/api/v2/projects/discord-py-interactions",
    ),
    "hikari": (
        "https://pypistats.org/packages/hikari",
        "https://api.pepy.tech/api/v2/projects/hikari",
    )
}


async def parsing_pypi(library: str) -> dict:

    async with aiohttp.ClientSession() as session:

        async with session.get(url=LINKS[library][0]) as request:
            soup1 = BeautifulSoup(await request.text(), "html.parser")

        async with session.get(url=LINKS[library][1]) as request:
            reqs = await request.text()
            reqs = json.loads(reqs)

    div1 = soup1.find("div", {"class": "wrapper"}).text.split()
    last_day = f"{date.today() - timedelta(days=1)}"

    downloads_list = reqs["downloads"][last_day]
    items_list = downloads_list.values()

    last_version2 = reqs["versions"]
    last_version2.sort(key=lambda x: tuple((x.lstrip("v") + "z").split(".")))
    last_version2 = last_version2[-1]
    try:
        if library == "disnake":

            return {"last_version": div1[29], "downloads": div1[59::4][1:], }, {
                "last_version": last_version2,
                "total_downloads": f"{reqs['total_downloads']:,d}",
                "downloads_sum": f"{sum(items_list):,d}",
                "last_version_downloads": f"{downloads_list[last_version2]:,d}",
                "set": last_day,
            }

        elif library == "nextcord":

            return {"last_version": div1[33], "downloads": div1[37::4], }, {
                "last_version": last_version2,
                "total_downloads": f"{reqs['total_downloads']:,d}",
                "downloads_sum": f"{sum(items_list):,d}",
                "last_version_downloads": f"{downloads_list[last_version2]:,d}",
                "set": last_day,
            }

        elif library == "pycord":

            return {"last_version": div1[29], "downloads": div1[51::4][1:], }, {
                "last_version": last_version2,
                "total_downloads": f"{reqs['total_downloads']:,d}",
                "downloads_sum": f"{sum(items_list):,d}",
                "last_version_downloads": f"{downloads_list[last_version2]:,d}",
                "set": last_day,
            }
        elif library == "discord.py":

            return {"last_version": div1[28], "downloads": div1[60::4][1:]}, {
                "last_version": last_version2,
                "total_downloads": f"{reqs['total_downloads']:,d}",
                "downloads_sum": f"{sum(items_list):,d}",
                "last_version_downloads": f"{downloads_list[last_version2]:,d}",
                "set": last_day,
            }

        elif library == "interactions.py":

            return {"last_version": div1[33], "downloads": div1[53::4][2:]}, {
                "last_version": last_version2,
                "total_downloads": f"{reqs['total_downloads']:,d}",
                "downloads_sum": f"{sum(items_list):,d}",
                "last_version_downloads": f"{downloads_list[last_version2]:,d}",
                "set": last_day,
            }

        elif library == "hikari":

            last_version2 = [i for i in reqs['versions']
                            if len(i) == 12 and 'dev' in i]
            last_version2.sort(key=lambda x: tuple((x + "z").split(".")))
            last_version2 = last_version2[-1]

            return {"last_version": div1[34], "downloads": div1[54::4]}, {
                "last_version": last_version2,
                "total_downloads": f"{reqs['total_downloads']:,d}",
                "downloads_sum": f"{sum(items_list):,d}",
                "last_version_downloads": f"{downloads_list[last_version2]:,d}",
                "set": last_day,
            }
    except Exception:
        return "not working"


async def parsing_downloads(library: str) -> Dict[str, int]:
    async with aiohttp.request("GET", LINKS[library][1]) as response:
        response = await response.text()
    response = json.loads(response)

    downloads_list = response['downloads']

    dates = [f"{date.today() - timedelta(days=i)}" for i in range(1, 31)]

    return {date: sum(downloads_list[date].values()) for date in dates}
