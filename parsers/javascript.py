import aiohttp
import asyncio

LINKS_DAY = {
    "discord.js": f"https://api.npmjs.org/downloads/point/last-day/discord.js",
    "eris": f"https://api.npmjs.org/downloads/point/last-day/eris"}

LINKS_WEEK = {
    "discord.js": f"https://api.npmjs.org/downloads/point/last-week/discord.js",
    "eris": f"https://api.npmjs.org/downloads/point/last-week/eris"}

LINKS_MONTH = {
    "discord.js": f"https://api.npmjs.org/downloads/point/last-month/discord.js",
    "eris": f"https://api.npmjs.org/downloads/point/last-month/eris"}

LINKS_REGISTRY = {
    "discord.js": "https://registry.npmjs.org/discord.js",
    "eris": "https://registry.npmjs.org/eris"
}

async def parsing_npm(library: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=LINKS_DAY[library]) as request:
            data = await request.json()
            day = f"{data['downloads']:,d}"

        async with session.get(url=LINKS_WEEK[library]) as request:
            data = await request.json()
            week = f"{data['downloads']:,d}"

        async with session.get(url=LINKS_MONTH[library]) as request:
            data = await request.json()
            month = f"{data['downloads']:,d}"
        
        async with session.get(url=LINKS_REGISTRY[library]) as request:
            data = await request.json()
            version = data["dist-tags"]["latest"]
    return {
        "last_version": version,
        "last_day": day,
        "last_week": week,
        "last_month": month,
    }