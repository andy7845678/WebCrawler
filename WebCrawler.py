import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")


soup = BeautifulSoup(r.text,"html.parser")
sel = soup.select("div.title a")

#for s in sel:
#    print(s["href"], s.text)


file = open('myfile.txt', 'w')
for s in sel:
    file.write(s["href"])
    file.write(s.text)
    file.write("\n")