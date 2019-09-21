import requests
from bs4 import BeautifulSoup
import json
import codecs
import datetime

url3='https://stopgame.ru/news'
def url_stuff(url):
    resp=requests.get(url)
    return resp
def parcer(url,resp):
    topics={}
    now = datetime.datetime.now()
    topics["url="]=[url]
    topics["Date"]=[str(now)]
    topics["Titles"]=[]
    resp=requests.get(url)
    if resp.status_code == 200:
        soup3 = BeautifulSoup(resp.text, 'html.parser')
        l3 = soup3.find("div", {"class": "lent-left"})
        for i in l3.findAll("div","title lent-title"):
            topics["Titles"].append({"Title": i.text})
    else:
        print("All for now")
    return topics
def write_json(topics):
    with codecs.open("StopGame.json", "w", encoding="utf-8") as outfile:
        json.dump(topics, outfile, indent=4, ensure_ascii=False, separators=(',', ': '))
    outfile.close()
resp3=url_stuff(url3)
top=parcer(url3,resp3)
write_json(top)
