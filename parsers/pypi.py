# libs
from bs4 import BeautifulSoup
import requests as req
import json
# parse

def parsing_pypi():
    response = req.get("https://api.pepy.tech/api/v2/projects/disnake").text
    reqs = json.loads(response)
    try:
        last_day = str(date.today())
        downloads_list = list(reqs["downloads"][last_day])
    except KeyError:
        last_day = str(date.today())[:-1] + str(int(str(date.today())[-1]) - 1)
        downloads_list = reqs["downloads"][last_day]
    items_list = list(downloads_list.values())
    return {
        "last_version": reqs['versions'][-1],
        "total_downloads": reqs['total_downloads'],
        "downloads_sum": sum(items_list),
        "last_version_downloads": downloads_list[reqs['versions'][-1]],
        "set": last_day,
    }
