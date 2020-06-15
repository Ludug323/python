import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.dcard.tw/f/show_cats")
soup = BeautifulSoup(r.text,"html.parser")                      #轉成html.parser
sel = soup.select("img.t5f2fb-0.kSmyau.sc-1v1d5rx-12.hNEazt")   #選擇關鍵字

address = input("輸入你要存放的路徑: ")
imgAddress = address + "/"
num = 0

for s in sel:
    num += 1
    imgSrc = s["src"]
    print(f"第{num}張 :",imgSrc)
    pic = requests.get(imgSrc)
    img = pic.content
    pic_out = open(imgAddress + "PetImg" + str(num) + ".gif",'wb')
    pic_out.write(img)
    pic_out.close()