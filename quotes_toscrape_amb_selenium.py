from typing import Text
#import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver_path =  'C:\\Users\\jordi\\Documents\\_JORDI\\UOC\\Master Data Science\\Tipologia i cicle de vida 2021\\Practica 1\\chromedriver.exe' #sys.argv[1]

options = Options()
options.headless = False
driver = webdriver.Chrome(chromedriver_path, options=options)

# def open_html(path):
#     with open(path, 'rb') as f:
#         return f.read()  
        
#page = html = open_html('quotes.html') 
#soup = BeautifulSoup(page, features="html.parser")
driver.get("http://quotes.toscrape.com/js") # amb /js-delayed hauriem d'afegir un time.sleep(10) després
soup = BeautifulSoup(driver.page_source, features="html.parser")

numelement = 0
numpg = 1
list_tags = []
# fa l'scraping de totes les quotes de la web passant cada pàgina
while True:

    divs = soup.find_all(attrs={'class':'quote'})
    for div in divs:
        text = div.find(attrs={'class':'text'})
        author = div.find(attrs={'class':'author'})
        print(str(numelement) + text.string)
        print(author.string)
        tags = div.find_all(attrs={'class':'tag'})
        for tag in tags:
            list_tags.append (tag.string)
        print (*list_tags, sep=", ") 
        list_tags.clear()
        numelement = numelement + 1
        print()

    if not (paginacio := soup.find(attrs={'class':'next'})) or numpg == 1:
        break
    a = paginacio.find('a') 
    driver.get("http://quotes.toscrape.com"+a['href']) 
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    numpg += 1
    time.sleep(1)

time.sleep(3)
driver.quit() 

  