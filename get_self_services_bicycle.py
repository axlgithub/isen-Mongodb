from Station import Station
import requests
import json  
from pymongo import MongoClient
import usefull_functions



######################################################################

##    Obtention du json contenant les stations de vélib de Lille  ####

######################################################################

def get_vlille():
    url="https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=3000&facet=libelle&facet=nom&facet=commune&facet=&etat&facet=type&facet=etatconnexion"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records",[])


#######################################################################

######################################################################

##    Obtention du json contenant les stations de vélib de Lyon  ####

######################################################################

def get_vlyon():
    url="http://api.citybik.es/v2/networks/velov"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    data=response_json.get("network",[])
    return (data["stations"])

######################################################################


##    Obtention du json contenant les stations de vélib de Rennes  ####

######################################################################

def get_vrennes():
    url="https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps-reel&q=&rows=300&facet=nom&facet=etat&facet=nombreemplacementsactuels&facet=nombreemplacementsdisponibles&facet=nombrevelosdisponibles"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records",[])


#######################################################################

####  Obtention du json contenant les stations de vélib de Paris  #####

#######################################################################


def get_vparis():
    url="https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&rows=300&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records",[])


########################################################################



########################################################################

###             Création de la db pour lille                      ######

########################################################################

def db_create_lille():
    vlille_list= get_vlille()
    dbname=usefull_functions.get_database("vélib")
    collection_name=dbname["Lille"]
    for x in vlille_list:
        collection_name.insert_one(Station(x["recordid"],
        x["fields"]["etat"],
        x["fields"]["nbvelosdispo"],
        x["fields"]["nbplacesdispo"]-x["fields"]["nbvelosdispo"],
        x["fields"]["nom"],
        x["fields"]["localisation"][0],
        x["fields"]["localisation"][1]).__dict__
        )
    return()


#########################################################################

#########################################################################

#####"               Création de la db pour Rennes                ########

#########################################################################
def db_create_rennes():
    vrennes_list=get_vrennes()
    dbname=usefull_functions.get_database("vélib")
    collection_name=dbname["Rennes"]
    for x in vrennes_list:
        collection_name.insert_one(Station(x["recordid"],
        x["fields"]["etat"],
        x["fields"]["nombrevelosdisponibles"],
        x["fields"]["nombreemplacementsdisponibles"],
        x["fields"]["nom"],
        x["fields"]["coordonnees"][0],
        x["fields"]["coordonnees"][1]).__dict__
        )
    return()
            


#########################################################################

#####"               Création de la db pour Lyon                ########

#########################################################################
def db_create_lyon():
    vlyon_list=get_vlyon()
    dbname=usefull_functions.get_database("vélib")
    collection_name=dbname["Lyon"]
    for x in vlyon_list:
        collection_name.insert_one(Station(x["id"],
        x["extra"]["status"],
        x["free_bikes"],
        x["empty_slots"],
        x["name"],
        x["latitude"],
        x["longitude"]).__dict__
        )
    return()


#########################################################################

#####"               Création de la db pour Paris                ########

#########################################################################
def db_create_paris():
    vparis_list=get_vparis()
    dbname=usefull_functions.get_database("vélib")
    collection_name=dbname["Paris"]
    for x in vparis_list:
        collection_name.insert_one(Station(x["recordid"],
        x["fields"]["is_renting"],
        x["fields"]["numbikesavailable"],
        x["fields"]["numdocksavailable"],
        x["fields"]["name"],
        x["fields"]["coordonnees_geo"][0],
        x["fields"]["coordonnees_geo"][1]).__dict__
        )
    return()


    
if __name__ == "__main__": 
    db_create_paris()
    db_create_lyon()
    db_create_lille()
    db_create_rennes()

