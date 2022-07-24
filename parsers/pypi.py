# libs
from bs4 import BeautifulSoup
from datetime import date, timedelta
import grequests as req
import json
import time

# links

links = {"disnake": ["https://pypistats.org/packages/disnake",
                     "https://api.pepy.tech/api/v2/projects/disnake"],

         "nextcord": ["https://pypistats.org/packages/nextcord",
                      "https://api.pepy.tech/api/v2/projects/nextcord"],

         "pycord": ["https://pypistats.org/packages/py-cord",
                    "https://api.pepy.tech/api/v2/projects/py-cord"],

         "discord.py": ["https://pypistats.org/packages/discord.py",
                        "https://api.pepy.tech/api/v2/projects/discord.py"],
         }

# parse


def parsing_pypi(library: str):

    link_get = [req.get(link) for link in links[library]]
    responses = req.map(link_get)

    soup1 = BeautifulSoup(responses[0].content, 'html.parser')
    reqs = responses[1].text
    reqs = json.loads(reqs)

    div1 = soup1.find("div", {"class": "wrapper"}).text.split()
    last_day = str(date.today() - timedelta(days=1))

    downloads_list = reqs["downloads"][last_day]
    items_list = list(downloads_list.values())

    if library == "disnake":

        last_version2 = reqs['versions'][-1]

        return {

            "last_version": div1[29],
            "downloads": div1[57::4],

        }, {

            "last_version": last_version2,
            "total_downloads": "{:,}".format(reqs['total_downloads']),
            "downloads_sum": "{:,}".format(sum(items_list)),
            "last_version_downloads": "{:,}".format(downloads_list[last_version2]),
            "set": last_day,

        }

    elif library == "nextcord":

        last_version2 = ([int(i.replace(".", ""))
                          for i in reqs['versions']
                          if i.replace(".", "").isdigit()])
        last_version2 = ".".join(str(sorted(last_version2)[-1]))

        return {

            "last_version": div1[33],
            "downloads": div1[37::4],

        }, {

            "last_version": last_version2,
            "total_downloads": "{:,}".format(reqs['total_downloads']),
            "downloads_sum": "{:,}".format(sum(items_list)),
            "last_version_downloads": "{:,}".format(downloads_list[last_version2]),
            "set": last_day

        }

    elif library == "pycord":

        last_version2 = ([int(i.replace(".", ""))
                          for i in reqs['versions']
                          if i.replace(".", "").isdigit()])
        last_version2 = ".".join(str(sorted(last_version2)[-1]))

        return {

            "last_version": div1[29],
            "downloads": div1[51::4][1:],

        }, {

            "last_version": last_version2,
            "total_downloads": "{:,}".format(reqs['total_downloads']),
            "downloads_sum": "{:,}".format(sum(items_list)),
            "last_version_downloads": "{:,}".format(downloads_list[last_version2]),
            "set": last_day

        }

    elif library == "discord.py":

        last_version2 = reqs['versions'][-1]

        return {

            "last_version": div1[28],
            "downloads": div1[40::4][1:]

        }, {

            "last_version": last_version2,
            "total_downloads": "{:,}".format(reqs['total_downloads']),
            "downloads_sum": "{:,}".format(sum(items_list)),
            "last_version_downloads": "{:,}".format(downloads_list[last_version2]),
            "set": last_day

        }
