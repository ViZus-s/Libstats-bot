from dateutil import parser
from typing import Dict
from disnake.utils import format_dt
from bs4 import BeautifulSoup
import requests as req

library_links: Dict[str, str] = {
    "disnake": "https://github.com/DisnakeDev/disnake/commit/master",
    "nextcord": "https://github.com/nextcord/nextcord/commit/master",
    "pycord": "https://github.com/Pycord-Development/pycord/commit/master",
    "discord.py": "https://github.com/Rapptz/discord.py/commit/master",
    "interactions.py": "https://github.com/interactions-py/library/commit/stable",
}


def parsing_git(library: str) -> Dict[str, str]:

    response = req.get(library_links[library])
    soup = BeautifulSoup(response.content, "html.parser")

    stars = soup.find("span", {"class": "Counter js-social-count"}).text
    forks = soup.find("span", {"class": "Counter"}).text
    issues = soup.find("span", {"id": "issues-repo-tab-count"}).text
    pull_requests = soup.find("a", {"id": "pull-requests-tab"}).text
    raw_last_commit = soup.find("relative-time")["datetime"]
    last_commit = format_dt(parser.parse(raw_last_commit), "R")

    return {
        "stars": stars,
        "forks": forks,
        "issues": issues,
        "pull requests": pull_requests.replace("\n", "")[13:],
        "last commit": last_commit,
    }


def parsing_update():

    response = req.get("https://github.com/ViZus-s/Libstats-bot/commit/main")
    soup = BeautifulSoup(response.content, "html.parser")

    return soup.find("div", {"class": "commit-title markdown-title"}).text.strip()
