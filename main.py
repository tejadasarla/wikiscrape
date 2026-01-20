from bs4 import BeautifulSoup
import requests

host = "https://en.wikipedia.org"


def href_filter(link: str):
    return link and link.startswith("/wiki/") and ":" not in link


start_url = "https://en.wikipedia.org/wiki/India"

res = requests.get(start_url, headers={
    "User-Agent": "Mozilla"
})
html = res.content.decode("utf-8")

bs = BeautifulSoup(html, "html.parser")
tags = bs.find_all("a", href=href_filter)
unique_hrefs = {tag["href"] for tag in tags}

for href in unique_hrefs:
    print(host+href)
