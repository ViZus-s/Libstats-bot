# libs
from bs4 import BeautifulSoup
import requests as req
# parse

def parsing_pypi():
    response = req.get("https://pypi.org/project/disnake/")
    soup = BeautifulSoup(response.content, 'html.parser')

    last_version = soup.find("h1", {"class":"package-header__name"}).text.strip().rstrip()
    status = soup.find("a", {"href":"/search/?c=Development+Status+%3A%3A+5+-+Production%2FStable"}).text.strip()
    
    return last_version[8:], status