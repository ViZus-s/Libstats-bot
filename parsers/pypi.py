# libs
from bs4 import BeautifulSoup
from datetime import date
import grequests as req
import json
import time

# links

links = ["https://pypistats.org/packages/disnake", 
"https://api.pepy.tech/api/v2/projects/disnake",]

# parse

def parsing_pypi():
    link_get = [req.get(link) for link in links]
    responses = req.map(link_get)
    
    soup1 = BeautifulSoup(responses[0].content, 'html.parser')
    reqs = responses[1].text
    reqs = json.loads(reqs)

    div1 = soup1.find("div", {"class": "wrapper"}).text.split()

    try:
        last_day = str(date.today())
        downloads_list = list(reqs["downloads"][last_day])
    except KeyError:
        last_day = str(date.today())[:-1] + str(int(str(date.today())[-1]) - 1)
        downloads_list = reqs["downloads"][last_day]
    items_list = list(downloads_list.values())

    return {
        "last_version": " ".join(div1[27:30])[16::],
        "downloads": div1[57::4],
    }, {
        "last_version": reqs['versions'][-1],
        "total_downloads": "{:,}".format(reqs['total_downloads']),
        "downloads_sum": "{:,}".format(sum(items_list)),
        "last_version_downloads": "{:,}".format(downloads_list[reqs['versions'][-1]]),
        "set": last_day,
    },
