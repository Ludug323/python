import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
search = input("請輸入要搜尋的商品: ")
page = input("請輸入搜尋到第幾頁: ")
headers ={
    'User-Agent' : 'Googlebot'
    #'page' : page
}
url = f"https://shopee.tw/search?keyword={search}&page={str(int(page)-1)}"

r = requests.get(url,headers = headers,allow_redirects = False)
soup = BeautifulSoup(r.text,"html.parser")

allItem = soup.select("div.col-xs-2-4.shopee-search-item-result__item")
title = soup.select("div._1NoI8_._16BAGk")
price = soup.select("span._341bF0")
itemLink = [i.find('a').get('href') for i in allItem]
for s in title:
    print(s.text)
'''
for t,p,l in zip(title,price,itemLink):
    print(t.text)
    print(p.text)
    print("https://shopee.tw/" + l)
    print("--------------------------")'''