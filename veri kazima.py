import shelve
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import urllib.request as urllib
class WebScrapper():
    def __init__(self):
        self.web_page = 'https://books.toscrape.com/index.html'
        self.get_soup(self.web_page)
        self.get_categories()
        self.create_db('Kitaplar')
        
        for a,b in self.dict.items():
            self.get_prices_stars(a,b)
            for i in range(len(self.list_1)):
                self.file_1[a] = self.list_1
        self.close_db()
    def get_soup(self,webpage):
        self.soup = BeautifulSoup
        self.soup_1 = self.soup(urllib.urlopen(webpage).read(), features="html.parser")
        return self.soup
    
    def get_categories(self):
        categories_list = self.soup_1.find("ul",{"class":"nav nav-list"}).find_all("a")
        self.dict = dict()
        for i in range(1,len(categories_list)):
            category = categories_list[i].string.strip().lower()+"_"+str(i+1)
            link = urljoin(self.web_page, categories_list[i].get("href"))
            self.dict[category] = link
        return self.dict
    
    def get_prices_stars(self,soup,link):
        soup_2 = self.soup(urllib.urlopen(link).read(), features="html.parser")
        self.list_1 = list()
        for dow in range(len(soup_2.find("ol", {"class":"row"}).find_all("h3"))):
            Name = soup_2.find("ol", {"class":"row"}).find_all("h3")[dow].string.strip()
            Rating = soup_2.find("ol", {"class":"row"}).find_all("p")[dow*3]["class"][1]
            Price = float(soup_2.find("ol", {"class":"row"}).find_all("p", {"class":"price_color"})[dow].string.strip().replace("£", ""))
            URL = urljoin(self.web_page, soup_2.find("ol", {"class":"row"}).find_all("h3")[dow].find("a").get("href").replace("../../..", ""))
            
            if Rating == "One":
                rating = 1
            elif Rating == "Two":
                rating = 2
            elif Rating == "Three":
                rating = 3
            elif Rating == "Four":
                rating = 4
            elif Rating == "Five":
                rating = 5
                self.list_1.append({'Name': Name, 'Rating': rating, 'Price': Price, 'URL':URL})
    def create_db(self, db_ismi):
        self.file_1 = shelve.open(db_ismi+".db", writeback=True, flag='c')
    def close_db(self):
        return self.file_1.close()
    def parse(self):
        file_2 = shelve.open("parse.db", writeback=True, flag='c')
        dict_2 = dict()
        for a,b in self.dict.items():
            list_2 = list()
            self.get_prices_stars(a,b)
            for i in range(len(self.list_1)):
                list_2.append({'Name': self.list_1[i]['Name'], 'Rating': self.list_1[i]['Rating'], 'Price': self.list_1[i]['Price']})
                dict_2[a] = list_2
            file_2[a] = list_2
        for k in file_2.keys():
            print("{}-{}".format(k,file_2[k]))
        file_2.close()
WebScrapper()
