from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver_path =  'C:\\Users\\jordi\\Documents\\_JORDI\\UOC\\Master Data Science\\Tipologia i cicle de vida 2021\\Practica 1\\chromedriver.exe' #sys.argv[1]

options = Options()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging']) #https://stackoverflow.com/questions/61561112/how-to-solve-getting-default-adapter-failed-error-when-launching-chrome-and-tr
driver = webdriver.Chrome(chromedriver_path, options=options)

def open_html(path):
     with open(path, 'rb') as f:
         return f.read()  
        
#opció temporal treballant amb algunes pàgines baixades de la web per fer les proves
#baseurl = 'https://rcdb.com'
#pgurl = '/r.htm?ot=2&ex'
baseurl ='file:///C:/Temp'
pgurl ='/rcbd_operating.htm'

driver.get(baseurl + pgurl) 
soup = BeautifulSoup(driver.page_source, features='html.parser')

features = ''
tracks = ''
#llista = ''
muntanya = ''
regio = []
div = soup.find(attrs={'class':'stdtbl'})
taula = div.table

#a partir de la primera taula que ens interessa recorrem les diferents files, sempre partint de la
#segona fila i de moment per la prova limitat a dos files mes
#de cada fila realment només ens interessa el primer link útil de la muntanya russa
#ja que hi entrarem a la pàgina de detall i n'extraurem allà tota la informació
for tr in taula.find_all('tr')[1:3]:
    # for td in tr.find_all('td')[1:]:        
    #     try:
    #         llista += td.text + ' '
    #     except:
    #         llista +=''
      ## pàgina detall
    a = tr.find_all('a')    
    driver.get(baseurl + a[1]['href']) 
    soup = BeautifulSoup(driver.page_source, features='html.parser')

    feature = soup.find(attrs={'id':'feature'})
    titol = feature.h1.text
    locations = feature.div.find_all('a') 
    parc = locations[0].text
    for tx in locations[1:]:
        regio.append(tx.get_text())
    data = feature.find('time').text
    textos = titol +' '+ parc+' '+','.join(regio)+' '+data
    features += textos + '\r\n'
    features += feature.ul.get_text() + '\r\n' #dades sobre els diferents tipus
    features += feature.ul.next_sibling.get_text() + '\r\n' #dades sobre la característica principal
    features += feature.ul.next_sibling.next_sibling.get_text() + '\r\n' #dades sobre fabricant i model
    tracks += soup.find('section').next_sibling.next_sibling.text + '\r\n' #secció amb la informació de les tracks
    muntanya += features + tracks + '\r\n'
    regio.clear()
    features = ''
    tracks = ''
print(muntanya)

time.sleep(3)
driver.quit()     
