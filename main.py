import requests
from bs4 import BeautifulSoup
import time
import threading

def web(WebUrl):
    
    url = WebUrl
    code = requests.get(url)
    content=code.content
    s = BeautifulSoup(content, "html.parser")
    span=s.find('span',class_='no-wrap').get_text()
    value=span[1:]
    localtime = time.asctime( time.localtime(time.time()))
    print(value)
    f=open("datafile.txt","a")
    f.write("\n\nTime:%s\nValue:%s" % (localtime,value))
    threading.Timer(30, web("https://www.coingecko.com/en/price_charts/bitcoin/inr")).start()

web("https://www.coingecko.com/en/price_charts/bitcoin/inr")