import requests
from bs4 import BeautifulSoup

def coinmarket(InCoin):
    lenCoin = len(InCoin)
    URL = "https://coinmarketcap.com/currencies/cardano/"
    page = requests.get(URL)
    scrapper = BeautifulSoup(page.content,"lxml")
    infos = scrapper.find_all("p")
    for info in infos:
        if(info.text[:lenCoin] == InCoin):
            print(info.text)