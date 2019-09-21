import requests
from bs4 import BeautifulSoup
import json
import codecs
import datetime
import unittest

class Finder(object):

    def __init__(self,url):
        self.url = url
    def url_stuff(self):
        resp = requests.get(self.url)
        return resp
    def parcer(self, resp):
        topics = {}
        now = datetime.datetime.now()
        topics["url="] = [self.url]
        topics["Date"] = [str(now)]
        topics["Titles"] = []
        resp = requests.get(self.url)
        if resp.status_code == 200:
            soup3 = BeautifulSoup(resp.text, 'html.parser')
            l3 = soup3.find("div", {"class": "lent-left"})
            for i in l3.findAll("div", "title lent-title"):
                topics["Titles"].append({"Title": i.text})
        else:
            print("All for now")
        return topics
    def write_json(self,topics):
        with codecs.open("StopGame.json", "w", encoding="utf-8") as outfile:
            json.dump(topics, outfile, indent=4, ensure_ascii=False, separators=(',', ': '))
        outfile.close()
def main():
    Parcer = Finder("https://stopgame.ru/news")
    resp3 = Parcer.url_stuff()
    top = Parcer.parcer(resp3)
    Parcer.write_json(top)
if __name__=="__main__":
    main()


'''class Parcer_test(Parcer_StopGame,unittest.TestCase):
    def test_parcer(url,topic):
            with codecs.open("StopGame.json", encoding="utf-8") as file:
                d = json.loads(file.read())
                for j in d["Titles"]:
                    resp = requests.get(url)
                    if resp.status_code == 200:
                        soup3 = BeautifulSoup(resp.text, 'html.parser')
                        l3 = soup3.find("div", {"class": "lent-left"})
                        for i in l3.findAll("div", "title lent-title"):
     test_parcer(url3,top)

    def __init__(self, url, height):
        # Необходимо вызвать метод инициализации родителя.
        # В Python 3.x это делается при помощи функции super()
        super().__init__(kind, height)'''