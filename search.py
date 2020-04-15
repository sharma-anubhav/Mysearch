import urllib
import requests, webbrowser
from bs4 import BeautifulSoup

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
while True:
    query = input("Search: ")
    query = query.replace(' ', '+')
    choice = input("what Would you like to see? TYPE: Web OR News OR Video: ")
    if choice == "web" or choice == "Web":
        URL = f"https://google.com/search?q={query}"
        headers = {"user-agent": USER_AGENT}
        resp = requests.get(URL, headers=headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            results = soup.select('.r a')
            for link in results[:3]:
                actual = link.get('href')
                print(actual)
                webbrowser.open(actual)

    elif choice == "News" or choice == "news":
        URL = f"https://google.com/search?q={query}" + "&tbm=nws&"
        headers = {"user-agent": USER_AGENT}
        resp = requests.get(URL, headers=headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
            results = soup.select('.lLrAF')
            for link in results[:4]:
                actual = link.get('href')
                print(actual)
                webbrowser.open(actual)

    elif choice == "Video" or choice == "video":
        URL = f"https://google.com/search?q={query}" + "&tbm=vid&"
        print(URL)
        headers = {"user-agent": USER_AGENT}
        resp = requests.get(URL, headers=headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
            results = soup.select('.rGhul')
            for link in results[:2]:
                actual = link.get('href')
                print(actual)
                webbrowser.open(actual)

# 5https://www.google.com/search?q=anubhav&tbm=isch&