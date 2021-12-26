import builtwith, requests, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Carrega global del chromedriver, és més eficient fer-ho així que carregar i tancar dins una funció cada cop
chromedriver_path =  './chromedriver.exe' 
options = Options()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging']) 
driver = webdriver.Chrome(chromedriver_path, options=options)

def web_technology_identifier(url):
    """
    Mostra informació de la tecnologia utilitzada en una web.
    :param url: link web a analitzar
    """

    d = builtwith.parse(url)

    print("\nThe technologies used by the website {} are:".format(url))

    for i, j in d.items():
        print("{}: {}".format(i, j))


def download_web_HTML(url):
    """
    This function will download the web page and return the HTML.
    Aquesta funcio descarrega una web i retorna el seu HTMl.
    :param url:
    :return:
    """
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        html = soup.prettify()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return html


def download_web_soup(url):
    """
    This function will download the web page and return the soup.
    Aquesta funcio descarrega una web i retorna l'objecte soup.
    :param url:
    :return:
    """
    try:      
        driver.get(url) 
        time.sleep(1) 
        soup = BeautifulSoup(driver.page_source, features='html.parser')
    except Exception as e:
        driver.quit()
        print (e.__doc__)
        raise SystemExit(e)

    return soup


def get_url_list(url_base, url, n):
    """
    Returns a list of web pages.
    Retorna una llista de webs.
    :param url_base: url base
    :url: url primera pàgina
    :param n: quantitat de pàgines a scrape
    :return:
    """
    urllist = [url]
    nxt = ''
    percentatge_descarrega = 0

    for i in range(n-1):
        soup = download_web_soup(url)
        foot = soup.find(attrs={'id': 'rfoot'})
        foot = foot.find_all('a')

        for el in foot:
            if '>>' in el.get_text():
                nxt = el.get('href')

        next_page = url_base + nxt
        urllist.append(next_page)
        url = next_page
        percentatge_descarrega = round(i / n * 100, 1)
        print("Retrieving coaster-web pages list to scrape: {} % completed".format(percentatge_descarrega))

    print("List completed.\n-----------------------------------------")

    return urllist
