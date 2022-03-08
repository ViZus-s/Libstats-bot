# libs
from bs4 import BeautifulSoup
import requests as req
# parse

def parsing_git():
    response = req.get("https://github.com/DisnakeDev/disnake/commit/master")
    soup = BeautifulSoup(response.content, 'html.parser')

    stars = soup.find("span", {'class': "Counter js-social-count"}).text
    forks = soup.find("span", {'class': "Counter"}).text
    issues = soup.find("span", {"id": "issues-repo-tab-count"}).text
    pull_requests = soup.find("a", {"id": "pull-requests-tab"}).text
    last_commit = str(soup.find("relative-time")).split(
        ">", maxsplit=1)[0].split("datetime=")[-1][1:-2].replace("T", " ")

    return print({"stars": stars,
                  "forks": forks,
                  "issues": issues,
                  "pull requests": pull_requests.replace("\n", "")[13:],
                  "last commit": last_commit})


def parsing_update():
    response = req.get(
        "https://github.com/ViZus-s/Disnake-Statistics-Bot/commit/")
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find('div', {"class": "commit-title markdown-title"}).text.strip()
