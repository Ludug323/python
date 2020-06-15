from selenium import webdriver
import time
import requests

driverPath = "D:\\chromedriver.exe" #填入剛剛記下的路徑
driver = webdriver.Chrome(driverPath)

driver.get("https://www.google.com")
time.sleep(2)#做完休息2秒

searchInput = driver.find_element_by_name("q")#利用driver尋找元素名字
searchInput.send_keys("python 爬蟲")
time.sleep(2)

searchBtn = driver.find_element_by_name("btnK")
searchBtn.click()#要求電腦做點擊動作

html = driver.page_source

#driver.close()