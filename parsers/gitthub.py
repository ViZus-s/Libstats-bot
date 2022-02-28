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
    last_commit = soup.find("relative-time").text

    return {"stars": stars,
            "forks": forks, 
            "issues": issues, 
            "pull requests": pull_requests.replace("\n", "")[13:], 
            "last commit": last_commit}