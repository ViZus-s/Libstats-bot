import aiohttp

from datetime import date, timedelta
from bs4 import BeautifulSoup

LINKS = {
    "Discord.Net": ("https://azuresearch-usnc.nuget.org/query?q=Discord.Net", ),
    "DSharpPlus": ("https://azuresearch-usnc.nuget.org/query?q=DSharpPlus", ),
}

# https://www.nuget.org
async def parsing_nuget(library: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=LINKS[library][0]) as request:
            data = await request.json()
            data = data["data"][0]

    last_version = data['version']
    total_downloads = data['totalDownloads']
    return {
        "last_version": last_version,
        "total_downloads": total_downloads
    }

# I will update this soon, if you have a package statistics site - dm me (ViZus#9667)
