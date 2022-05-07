# libs
from bs4 import BeautifulSoup
import requests as req
# parse

def parsing_pypi():
    response = req.get("https://pypistats.org/packages/disnake")
    soup = BeautifulSoup(response.content, 'html.parser')

    div = soup.find("div", {"class": "wrapper"}).text.split()

    return {
        "last_version": " ".join(div[27:30])[16::],
        "downloads": div[57::4],
    }
