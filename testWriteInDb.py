from Station import Station
import requests
import json
from pprint import pprint  
import time

#############################################################################

###        get_database, from https://www.mongodb.com/languages/python ######

#############################################################################

def get_database(name_of_data_base):
    from pymongo import MongoClient
    import pymongo

    #Get the password and the username in a file next to this python script 
    pwd_file = open('test2','r')
    pwd=(pwd_file.readline()).strip("\n")
    username=(pwd_file.readline()).strip("\n")
    pwd_file.close()

    #Fabrication of the connection string used to connect ourselves with our password and login to the database
    CONNECTION_STRING = "mongodb+srv://"+username+":"+pwd+"@cluster0.dragk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)

    #return the database asked in parameter
    return client[name_of_data_base]





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
    dbname=get_database("vélib")
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
    dbname=get_database("vélib")
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
    dbname=get_database("vélib")
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
    dbname=get_database("vélib")
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

#########################################################################





#############################################################################

###        update                                                      ######

#############################################################################

def update(city):
    if city == "Paris":
        new_data = get_vparis()
        dbname=get_database("vélib")
        collection = dbname["Paris"]
        for x in new_data:
            name_of_the_station = x["fields"]["name"]
            number_of_available_places = x["fields"]["numdocksavailable"]
            number_of_bikes_availables = x["fields"]["numbikesavailable"]
            etat=x["fields"]["is_renting"]
            new_values1 = {"$set": {'places_dispo': number_of_available_places}}
            new_values2 = {"$set": {'velos_dispo': number_of_bikes_availables}}
            new_values3 = {"$set": {'etat': etat}}
            print(name_of_the_station)
            collection.update_one({'nom': name_of_the_station}, new_values1)
            collection.update_one({'nom': name_of_the_station}, new_values2)
            collection.update_one({'nom': name_of_the_station}, new_values3)
    if city == "Lille":
        new_data = get_vlille()
        dbname=get_database("vélib")
        collection = dbname["Lille"]
        for x in new_data:
            name_of_the_station = x["fields"]["nom"]
            number_of_available_places = x["fields"]["nbplacesdispo"]-x["fields"]["nbvelosdispo"]
            number_of_bikes_availables = x["fields"]["nbvelosdispo"]
            etat=x["fields"]["etat"]
            new_values1 = {"$set": {'places_dispo': number_of_available_places}}
            new_values2 = {"$set": {'velos_dispo': number_of_bikes_availables}}
            new_values3={"$set": {'etat': etat}}
            print(name_of_the_station)
            collection.update_one({'nom': name_of_the_station}, new_values1)
            collection.update_one({'nom': name_of_the_station}, new_values2)
            collection.update_one({'nom': name_of_the_station}, new_values3)
    if city == "Lyon":
        new_data = get_vlyon()
        dbname=get_database("vélib")
        collection = dbname["Lyon"]
        for x in new_data:
            name_of_the_station = x["name"]
            number_of_available_places = x["empty_slots"]
            number_of_bikes_availables = x["free_bikes"]
            etat=x["extra"]["status"]
            new_values1 = {"$set": {'places_dispo': number_of_available_places}}
            new_values2 = {"$set": {'velos_dispo': number_of_bikes_availables}}
            new_values3 = {"$set": {'etat': etat}}
            print(name_of_the_station)
            collection.update_one({'nom': name_of_the_station}, new_values1)
            collection.update_one({'nom': name_of_the_station}, new_values2)
            collection.update_one({'nom': name_of_the_station}, new_values3)
    if city == "Rennes":
        new_data = get_vrennes()
        dbname=get_database("vélib")
        collection = dbname["Rennes"]
        for x in new_data:
            name_of_the_station = x["fields"]["nom"]
            number_of_available_places = x["fields"]["nombreemplacementsdisponibles"]
            number_of_bikes_availables = x["fields"]["nombrevelosdisponibles"]
            etat=x["fields"]["etat"]
            new_values1 = {"$set": {'places_dispo': number_of_available_places}}
            new_values2 = {"$set": {'velos_dispo': number_of_bikes_availables}}
            new_values3={"$set": {'etat': etat}}
            print(name_of_the_station)
            collection.update_one({'nom': name_of_the_station}, new_values1)
            collection.update_one({'nom': name_of_the_station}, new_values2)
            collection.update_one({'nom': name_of_the_station}, new_values3)
         


##############################################################################


#############################################################################

###        capture                                                     ######

#############################################################################

def capture(city):
    if city == "Paris":
        new_data = get_vparis()
        dbname=get_database("vélib")
        collection = dbname["capture"]
        for x in new_data:
            i=int(time.time())
            collection.insert_one(Station(x["recordid"]+str(i),
            x["fields"]["is_renting"],
            x["fields"]["numbikesavailable"],
            x["fields"]["numdocksavailable"],
            x["fields"]["name"],
            x["fields"]["coordonnees_geo"][0],
            x["fields"]["coordonnees_geo"][1]).__dict__
        )
    if city == "Lille":
        new_data = get_vlille()
        dbname=get_database("vélib")
        collection = dbname["capture"]
        for x in new_data:
            i=int(time.time())
            collection.insert_one(Station(x["recordid"]+str(i),
            x["fields"]["etat"],
            x["fields"]["nbvelosdispo"],
            x["fields"]["nbplacesdispo"]-x["fields"]["nbvelosdispo"],
            x["fields"]["nom"],
            x["fields"]["localisation"][0],
            x["fields"]["localisation"][1]).__dict__
        )
    if city == "Lyon":
        new_data = get_vlyon()
        dbname=get_database("vélib")
        collection = dbname["capture"]
        for x in new_data:
            i=int(time.time())
            collection.insert_one(Station(x["id"]+str(i),
            x["extra"]["status"],
            x["free_bikes"],
            x["empty_slots"],
            x["name"],
            x["latitude"],
            x["longitude"]).__dict__
            )
    if city == "Rennes":
        new_data = get_vrennes()
        dbname=get_database("vélib")
        collection = dbname["capture"]
        for x in new_data:
            i=int(time.time())
            collection.insert_one(Station(x["recordid"]+str(i),
            x["fields"]["etat"],
            x["fields"]["nombrevelosdisponibles"],
            x["fields"]["nombreemplacementsdisponibles"],
            x["fields"]["nom"],
            x["fields"]["coordonnees"][0],
            x["fields"]["coordonnees"][1]).__dict__
        )
           
         


##############################################################################






#############################################################################

###        clear                                                       ######

#############################################################################

def clear(collection_name):
    dbname=get_database("vélib")
    collection = dbname[collection_name]
    collection.drop()
    
           
         


##############################################################################







    
if __name__ == "__main__": 
    db_create_lyon()

"""
dbname=get_database("vélib")
    collection=dbname["Lille"]
    collection.drop()
    vlille_list= get_vlille()
    dbname=get_database("vlille")
    collection_name=dbname["station"]
    for k in range(len(vlille_list)):
        collection_name.insert_one(vlille_list[k])
    
    
     
    station = new_station("En service", "rue mace", 10)
    dbname = get_database("test")
    print(dbname)
    collection_name= dbname["station"]
    collection_name.insert_one(station)
"""