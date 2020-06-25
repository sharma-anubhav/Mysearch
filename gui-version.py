import tkinter as tk
import requests, webbrowser
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import os
import urllib

def sclick():
    # desktop user-agent
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    # mobile user-agent
    MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
    query = searchbar.get()
    query = query.replace(' ', '+')
    choice = var.get()
    if choice == 1 :
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

    elif choice == 2:
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

    elif choice == 3:
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

root = tk.Tk()
root.title("My Search")

canvas = tk.Canvas(root , height = 70 , width = 1024)
canvas.pack()


searchbar = tk.Entry(root , bg ='white')
searchbar.place(relx = 0.01 , rely = 0.1 , relwidth = 0.75)

search = tk.Button(root , text = "Search" , bg = 'white', fg = 'black' , command = sclick)
search.place(relx = 0.76 , rely = 0.1 , relwidth = 0.23)

var = tk.IntVar()
R1 = tk.Radiobutton(root, text="Web", variable=var, value= 1 ,bg ='#368BC1')
R1.place( relx = 0.01 , relwidth = 0.33 , rely = 0.55)

R2 = tk.Radiobutton(root, text="News", variable=var, value= 2 ,bg ='#368BC1')
R2.place( relx = 0.34 , relwidth = 0.33 , rely = 0.55)

R3 = tk.Radiobutton(root, text="Video", variable=var, value= 3 ,bg ='#368BC1')
R3.place( relx = 0.67 , relwidth = 0.32 , rely = 0.55)


root.mainloop()
