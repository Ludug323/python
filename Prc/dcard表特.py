import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.dcard.tw/f/beauty")
soup = BeautifulSoup(r.text,"html.parser")
sel = soup.select("img.t5f2fb-0.kSmyau.sc-1v1d5rx-12.hNEazt")
imgNum = 0
address = input("輸入你要存放的路徑: ")
imgAddress = address + "/"
for s in sel:
    if sel[0] == s:
        continue
    imgNum += 1
    imgSrc = s["src"]
    print(f"第{imgNum}張 : ",imgSrc)
    pic = requests.get(imgSrc)
    img = pic.content

    pic_out = open(imgAddress+"img"+str(imgNum)+".gif","wb")
    pic_out.write(img)
    pic_out.close()