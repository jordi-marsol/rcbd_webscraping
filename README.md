# Pràctica 1: Web scraping

## Context
Aquest repositori es realitza en el marc de la Pràctica 1 de la assignatura _Tipologia i cicle de vida de les dades_ del Màster en Ciència de Dades de la UOC.  Consisteix en aplicar diferents tècniques i llibreries amb llenguatge de programació Python per tal d'extreure dades d'un lloc web mitjançant eines de _web scraping_ i exportar-les a un dataset. En el nostre cas: 
extraurem dades del web <https://rcdb.com> (_Roller Coaster Data Base_): 
d'ara en endavant l'anomenarem _RCDB_.

--Aquest lloc web és una base de dades que conté més de 10.000 muntanyes russes de tot el món amb les seves característiques. Ha estat el·laborada de manera particular per diversos aficionats que la van actualitzant constantment i posa de manifest l'interès que pot tenir aquesta manera de divertir-se.

## Títol del dataset
--Muntanyes Russes operatives del web Roller Coaster DataBase /món

## Descripció del dataset.
--El dataset conté diverses dades referents a moltes de les muntanyes russes operatives que hi ha actualment al món. El lloc des d'on extraiem les dades contempla també muntanyes russes que ja no son operatives però aqui ens limitem a les que son vigents. Igualment donada la naturalesa educativa de la pràctica no preten ser una extracció exhaustiva de les dades que conté el lloc i està limitada a un determinat nombre de característiques i a un nombre limitat de pàgines. 

## Representació gràfica
--Fer un diagrama gràfic de quin procés es fa d'extracció i algunes captures del lloc web: 
per exemple al llistat i el detall de la pàgina.

| Muntanya Russa   		| Parc           	| Ubicació  				| Altura 		| Fabricant | Any | (...) 
| :-------------:		|:-------------		| :-----					| ---:			| --- 		| --- |  ---
| Dragon Khan			| PortAventura 		| Salou: 
Catalunya: 
Espanya | 45,1 m		| B&M 		| 1995 |
| Kingda Ka    			| Six Flags Great Adventure |   Jackson: 
New Jersey: 
USA | 139,0 m| Intamin AG | 2005 | 
| Steel Vengeance		| Cedar Point      | Sandusky: 
Ohio: 
USA		| 62,5 m		| RMC 		| 2018 | 
| (...)	|       | | 		|  		|  | 

## Contingut

### Camps

_Muntanya_russa_: Nom de la muntanya
_Ubicacio_: Ubicació de la muntanya. Aquesta inclou diferents localitzacions com ara població, regió local i país, en aquest ordre normalment, però depen del lloc on estigui en pot tenir més o menys.
_parc_: Nom del parc d'atraccions on està ubicada.
_Tipus_: Tipus de muntanya russa referit al material principal en què està fabricada.
_Data_obertura_: La data d'inauguració de la muntanya.
_Disseny_,_Fabricant_: El disseny i fabricant.
_Model_: El model
_Velocitat_màxima (mph)_: La velocitat màxima que pot assolir en milles per hora.
_Llargada (ft)_,_Altura_màxima (ft)_: La llargada màxima que té i l'alçada màxima.
_Inversions_: Inversions (girs) que té la muntanya.
_Duració_: Duració en minuts de tot el recorregut.
_Elements_: Elements de què està composta la muntanya.

### Periode de temps
El periode de temps en que es genera el contingut del scraping és aquell en que s'executa l'aplicació. No hi ha la intenció de limitar la cerca en un període de temps determinat però si en el nombre de pàgines que s'extreuen. La web de rcdb.com actualiza freqüentment els canvis i noves muntanyes russes per tant la informació que s'extregui en executar l'aplicació suposem que serà el més actual possible.

### Com s'ha recollit
El primer problema és que en fer un scraping amb la llibreria _requests_ directament la taula que mostra pel llistat els _tags_ <tr> no estan tancats i no es pot fer un bon seguiment dels elements, per això millor fem servir la funció _prettify_ que ens presenta correctament la jerarquia dels elements.

El lloc fa servir molt pocs identificadors únics per tant ens hem d'anar movent entre elements de manera relativa o en funció dels textos que apareixen.

L'altre problema és que no sempre surt tota la informació en tots els camps per tant en escanejar un valor pot ser que esperem que aparegui un però no hi sigui. Quan això passa omplim el valor amb el text _NA_

## Agraïments

[RCDB](https://rcdb.com) és una gran base de dades de muntanyes russes d'arreu del món. Inclou informació detallada de milers d'aquestes màquines de diversió com per exemple: la seva altura: 
longitud: 
ubicació: 
velocitat màxima: 
fabricant: 
any d'inauguració: 
dissenyador...

Presenta una política de completa permissivitat amb bots: 
segons indica el seu [robots.txt](https://rcdb.com/robots.txt): 
cosa que agraïm a l'hora de fer _web scraping_ :
```
User-agent: *
Disallow:
```
Hem pogut trobar un projecte de _scrape_ similar de muntanyes russes nord-americanes (<https://github.com/aarmora/jordan-scrapes-rcdb>) però està exportat a .json.

--Donat que es tracta d'un lloc no comercial no voldriem abusar dels recursos del lloc web per fer la extracció. Creiem que si se'n vulgués fer una extracció completa possiblement per algun us més comercial seria preferible contactar amb els autors de la pàgina.
Com indica als termes d'us: _Using the content to construct other databases: 
websites or applications requires prior written permission._

## Inspiració

Tot i ser una base de dades bastant extensa: 
no disposa d'un API per a descarregar les dades ni d'eines per fer anàlisis profunds amb les seves dades. És per això i sumat el fet que està plenament codificat en HTML: 
que ens ha semblat un bon web des d'on iniciar i practicar el _web scraping_ . 

Intentarem crear un dataset de muntanyes russes globals des del que es pugui fer anàlisis profunds de les muntanyes russes que hi ha al món.

A partir d'aquest dataset es podrien respondre: 
per exemple: 
les següents preguntes:
* _Quina és la evolució de la altura (o longitud: 
o velocitat màxima...) de les muntanyes russes al llarg de la història?_
* _Quins dissenyadors construeixen muntanyes russes més altes (o llargues: 
o ràpides...)?_
* _Si es vol contractar una constructora de muntanyes russes: 
quina és la empresa que té més experiència en muntanyes russes de fusta?_

Entre d'altres...

## Llicència

--Es farà servir una llicència pels datasets de tipus "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International" (CC BY-NC-SA)

La motivació del seu us ve pel fet principal que l'scraping s'ha fet a partir d'un interès educatiu i per tant no es permet un us comercial d'aquest. També es requereix la citació dels autors originals i que qualsevol transformació o addició del codi original ha de seguir tenint el mateix tipus de llicència


## Participants

|Contribucions|Signatura
|---|---
|Investigació prèvia|ARC,JML|
|Redacció de les respostes|ARC,JML|
|Desenvolupament del codi|ARC,JML|

## Codi
--Adjuntar al repositori Git el codi

## Dataset
--Publicar el dataset en _CSV_ a Zenodo amb una descripció


# Contingut per posar a readme.md

## Membres de l'equip
* **Jordi Marsol López**

* **Arnau Rafi Cuello**

## Fitxers


## Ubicació del dataset
(DOI de Zenodo del dataset)

## Recursos
(posar aquest apartat al readme.MD i no al pdf final.)

1. Lawson: 
R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel: 
R. (2015). _Web Scraping with Python: Collecting Data from the Modern Web_. O'Reilly Media: 
Inc. Chapter 1. Your First Web Scraper.
