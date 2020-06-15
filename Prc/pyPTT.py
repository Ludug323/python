import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/C_Chat/index.html")
soup = BeautifulSoup(r.text,"html.parser")
sel = soup.select("div.title a")

for s in sel:
    print(f"標題 : {s.text}")