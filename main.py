import func
import re
import os
import time
import pandas as pd
from bs4 import BeautifulSoup

# Requisits: Requereix Python 3.9 o superior
# La següent URL és la web resultat d'aplicar una cerca al buscador de rcdb.com,
# amb els següents criteris:
#   Criteria:	Existing
#               Roller Coasters
#               Current Status = Operating
#   Found:	5447 (Page 1 of 227)
#   Sorted By:	Opened
url = "https://rcdb.com/r.htm?order=8&st=93&ot=2&ex"
url_base = "https://rcdb.com/"

quantitat_de_pagines = 1           # Quantitat de pàgines a scrapejar
quantitat_de_coasters_x_pag = 10    # Quantitat de coasters a scrapejar per pàgina (24 és el màxim)

qty_coasters = quantitat_de_pagines * quantitat_de_coasters_x_pag

# Llista de pàgines a fer scrape:
urls_to_scrape = func.get_url_list(url_base, url, quantitat_de_pagines)

# Inicialitzo llista de llistes per emmagatzemar les dades de cada roller coaster:
data = []

# Inicialitzo alguns valors de dades:
length = 'NA'
height = 'NA'
qty_inversions = 'NA'
duration = 'NA'
elements = 'NA'
speed = 'NA'
fabricant = 'NA'
model = 'NA'

i = 0

for url in urls_to_scrape:

    # Descarrego sopa de url:
    soup = func.download_web_soup(url)

    # Scrape de la taula:
    table = soup.find(attrs={'class': 'stdtbl'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    # Aquest bucle recorre cada fila del body de la taula:
    for row in rows[0:quantitat_de_coasters_x_pag]:
        a = row.find_all('a')
        i += 1

        # Reinicialitzo tot els valors de les variables:
        nom_muntanya = 'NA'
        ubicacio = 'NA'
        park = 'NA'
        tipu = 'NA'
        data_obert = 'NA'
        disseny = 'NA'
        length = 'NA'
        height = 'NA'
        qty_inversions = 'NA'
        duration = 'NA'
        elements = 'NA'
        speed = 'NA'
        fabricant = 'NA'
        model = 'NA'

        # Petit algoritme que mou "cursor" en cas de que el primer camp de la fila no tingui "càmara":
        ini = -1
        if "Camera Icon" in a[0].prettify():
            ini = 0

        # Obtenció de dades que es troben directament a la taula:
        nom_muntanya = a[1 + ini].get_text()
        park = a[2 + ini].get_text()
        tipu = a[3 + ini].get_text()
        disseny = a[4 + ini].get_text()
        data_obert = row.find("time")["datetime"]
        url_coaster = a[1 + ini]['href']

        # Descàrrega de cada url_coaster
        percentatge_descarrega = round(i/qty_coasters * 100, 1)
        print("{}% \tDownloading data from: {}  \tRoller coaster: {}".format(percentatge_descarrega,
                                                                           url_base + url_coaster,
                                                                           nom_muntanya))
        soup_coaster = func.download_web_soup(url_base + url_coaster)

        feature = soup_coaster.find(attrs={'id': 'feature'})

        # Extracció de la ubicació:
        locations = feature.div.find_all('a')
        ubicacio = ''
        for tx in locations[1:]:
            ubicacio = ubicacio + tx.get_text() + ' / '
        ubicacio = ubicacio.removesuffix(' / ')

        try:
            # Extracció del fabricant:
            if "Make:" in feature.prettify():
                if "Make: " in feature.find(attrs={'class': 'scroll'}).find('p').get_text():
                    fabricant = feature.find(attrs={'class': 'scroll'}).find('a').get_text()

            # Extracció del model:
            if "Model:" in feature.prettify():
                if "Model: " in feature.find(attrs={'class': 'scroll'}).find('p').get_text():
                    model = feature.find(attrs={'class': 'scroll'}).find_all('a')[1].get_text()

            # Extracció de la info de la secció "tracks":
            if "Tracks" in soup_coaster.find_all('section')[1].find('h3').get_text():
                tracks = soup_coaster.find_all('section')[1]

                table_tracks = tracks.find(attrs={'class': 'stat-tbl'})
                table_tracks_body = table_tracks.find('tbody')
                rows_tracks = table_tracks_body.find_all('tr')

                length = 'NA'
                height = 'NA'
                qty_inversions = 'NA'
                duration = 'NA'
                elements = 'NA'
                speed = 'NA'

                for rowt in rows_tracks:
                    rowt_str = rowt.get_text()

                    if rowt_str.startswith("Length"):
                        length = rowt.find(attrs={'class': 'float'}).get_text()
                    elif rowt_str.startswith("Height"):
                        height = rowt.find(attrs={'class': 'float'}).get_text()
                    elif rowt_str.startswith("Speed"):
                        speed = rowt.find(attrs={'class': 'float'}).get_text()
                    elif rowt_str.startswith("Inversions"):
                        qty_inversions = re.findall(r'[0-99]', rowt.td.get_text())[0]
                    elif rowt_str.startswith("Duration"):
                        duration = re.findall(r'\d{1,2}:\d{1,2}', rowt.td.get_text())[0]
                    elif rowt_str.startswith("Elements"):
                        elements = ''
                        lst_elements = rowt.find_all('a')

                        for elem in lst_elements:
                            elements += elem.get_text() + '; '
                        elements = elements.removesuffix('; ')
        except Exception as e:
            print (e.__doc__)

        # Càrrega de dades:
        coaster = [nom_muntanya, ubicacio, park, tipu, data_obert, disseny, fabricant,
                   model, speed, length, height, qty_inversions, duration, elements]

        data.append(coaster)

func.driver.quit() # Aquí es tanca el chrome
dataset = pd.DataFrame(data, columns=["Muntanya_russa", "Ubicacio", "Parc", "Tipus", "Data_obertura", "Disseny",
                                      "Fabricant", "Model", "Velocitat_màxima (mph)", "Llargada (ft)",
                                      "Altura_màxima (ft)", "Inversions", "Duració", "Elements"])

dataset.to_csv("RollerCoasters.csv", sep=',', encoding='utf-8')

print("\nScraped {} pages.\nScraped {} roller coasters.".format(quantitat_de_pagines, qty_coasters))
print("\n-------------------------------------------------------------------------------------")
print("You can find resulting dataset 'RollerCoasters.csv' in the project base folder.")
print("This file has a size of {} bytes.".format(os.path.getsize(r'RollerCoasters.csv')))
