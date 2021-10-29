# Pràctica 1: Web scraping

## Context
Aquest repositori es realitza en el marc de la Pràctica 1 de la assignatura _Tipologia i cicle de vida de les dades_ del Màster en Ciència de Dades de la UOC.  Consisteix en aplicar diferents tècniques i llibreries amb llenguatge de programació Python per tal d'extreure dades d'un lloc web mitjançant eines de _web scraping_ i exportar-les a un dataset. En el nostre cas, extraurem dades del web <https://rcdb.com> (_Roller Coaster Data Base_), d'ara en endevant l'anomenarem "RCDB".

## Títol del dataset
_RollerCoasters.csv_

## Descripció del dataset.
--ddd

## Representació gràfica

| Muntanya Russa   		| Parc           	| Ubicació  				| Altura 		| Fabricant | Any | (...) 
| :-------------:		|:-------------		| :-----					| ---:			| --- 		| --- |  ---
| Dragon Khan			| PortAventura 		| Salou, Catalunya, Espanya | 45,1 m		| B&M 		| 1995 |
| Kingda Ka    			| Six Flags Great Adventure |   Jackson, New Jersey, USA | 139,0 m| Intamin AG | 2005 | 
| Steel Vengeance		| Cedar Point      | Sandusky, Ohio, USA		| 62,5 m		| RMC 		| 2018 | 
| (...)	|       | | 		|  		|  | 

## Contingut
--camps, periode de temps i  i com s'ha recollit

## Agraïments

[RCDB](https://rcdb.com) és una gran base de dades de muntanyes russes d'arreu del món. Inclou informació detallada de milers d'aquestes màquines de diversió com per exemple: la seva altura, longitud, ubicació, velocitat màxima, fabricant, any d'inauguració, dissenyador...

Presenta una política de completa permissivitat amb bots, segons indica el seu [robots.txt](https://rcdb.com/robots.txt), cosa que agraïm a l'hora de fer _web scraping_ :
```
User-agent: *
Disallow:
```
Hem pogut trobar un projecte de _scrape_ similar de muntanyes russes nord-americanes (<https://github.com/aarmora/jordan-scrapes-rcdb>) però està exportat a .json.

## Inspiració

Tot i ser una base de dades bastant extensa, no disposa d'un API per a descarregar les dades ni d'eines per fer anàlisis profunds amb les seves dades. És per això i sumat el fet que està plenament codificat en HTML, que ens ha semblat un bon web des d'on iniciar i practicar el _web scraping_ . 

Intentarem crear un dataset de muntanyes russes globals des del que es pugui fer anàlisis profunds de les muntanyes russes que hi ha al món.

A partir d'aquest dataset es podrien respondre, per exemple, les següents preguntes:
* _Quina és la evolució de la altura (o longitud, o velocitat màxima...) de les muntanyes russes al llarg de la història?_
* _Quins dissenyadors construeixen muntanyes russes més altes (o llargues, o ràpides...)?_
* _Si es vol contractar una constructora de muntanyes russes, quina és la empresa que té més experiència en muntanyes russes de fusta?_

Entre d'altres...

## Llicència
--cc

## Participants

|Contribucions|Signatura|
|Investigació prèvia|ARC,JML|
|Redacció de les respostes|ARC,JML|
|Desenvolupament del codi|ARC,JML|

## Codi
Adjuntar al repositori Git el codi

## Dataset
Publicar el dataset en _CSV_ a Zenodo amb una descripció


# Contingut per posar a readme.md

## Membres de l'equip
* **Jordi Marsol López**

* **Arnau Rafi Cuello**

## Fitxers
(Contingut temporal)

* **19235.htm**: prova de la pràctica ja minimanent funcional
* **rcbd_operating.htm**: prova de la pràctica ja minimanent funcional
* **3111.htm**: prova de la pràctica ja minimanent funcional
* **notes.txt**: arxiu de notes amb informació sobre actualitzacions i issues trobats
* **rcdb.py**: arxiu de python comentat. En aquesta primera versió no s'entra al detall de quina informació volem mostrar definitivament o de com queda presentada. Tampoc està polit a nivell de programació ni d'organització dels arxius ja que bàsicament és per provar fins on podem arribar i com de factible és l'scraping. 

Treballo amb tres arxius html que son copia del contingut de la web original per fer les proves, però es pot canviar ràpidament a la web real canviant el valor a les variables corresponents de l'aplicació. La idea final seria poder separar cada informació de les muntanyes ruses en un arxiu format .csv que podria quedar amb aquests camps, p.ex: nommuntanya, parc, localitzacions, datainici, tipus, tipusprincipal, fabricantmodel, tracks (desglossat en altres camps)

## Ubicació del dataset
(DOI de Zenodo del dataset)

## Recursos
(crec que no cal aquest apartat)

1. Lawson, R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel, R. (2015). _Web Scraping with Python: Collecting Data from the Modern Web_. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.
