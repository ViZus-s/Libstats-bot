# libs
from bs4 import BeautifulSoup
import requests as req
import time

# parse


def parsing_git(library: str):
    if library == "disnake":
        response = req.get(
            "https://github.com/DisnakeDev/disnake/commit/master")

    elif library == "nextcord":
        response = req.get(
            "https://github.com/nextcord/nextcord/commit/master")

    elif library == "pycord":
        response = req.get(
            "https://github.com/Pycord-Development/pycord/commit/master")

    soup = BeautifulSoup(response.content, 'html.parser')

    stars = soup.find("span", {'class': "Counter js-social-count"}).text
    forks = soup.find("span", {'class': "Counter"}).text
    issues = soup.find("span", {"id": "issues-repo-tab-count"}).text
    pull_requests = soup.find("a", {"id": "pull-requests-tab"}).text

    last_commit = str(soup.find("relative-time")).split(
        ">", maxsplit=1)[0].split("datetime=")[-1][1:-2].replace("T", " ")

    last_commit = f"<t:{int(time.mktime(time.strptime(last_commit, '%Y-%m-%d %H:%M:%S')))}>"

    return {"stars": stars,
            "forks": forks,
            "issues": issues,
            "pull requests": pull_requests.replace("\n", "")[13:],
            "last commit": last_commit, }


def parsing_update():
    response = req.get(
        "https://github.com/ViZus-s/Libstats-bot/commit/main")
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find('div', {"class": "commit-title markdown-title"}).text.strip()
