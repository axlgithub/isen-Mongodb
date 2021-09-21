import requests
import json
from pprint import pprint  


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

#################################



#############################################################################

###        new_station                                                 ######

#############################################################################

def new_station(state,name,size):
    new_station = {
        "state": state,
        "name": name,
        "size": size}  
    return new_station



##############################################################################




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
    url="https://transport.data.gouv.fr/gbfs/lyon/gbfs.json"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records",[])

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
    for k in range(len(vlille_list)):
        collection_name.insert_one(vlille_list[k])
    return()

#########################################################################

#########################################################################

#####"               Création de la db pour Rennes                ########

#########################################################################
def db_create_rennes():
    vrennes_list=get_vrennes()
    dbname=get_database("vélib")
    collection_name=dbname["Rennes"]
    for k in range(len(vrennes_list)):
        collection_name.insert_one(vrennes_list[k])
    return()


#########################################################################

#####"               Création de la db pour Lyon                ########

#########################################################################
def db_create_lyon():
    vlyon_list=get_vlyon()
    dbname=get_database("vélib")
    collection_name=dbname["Lyon"]
    for k in range(len(vlyon_list)):
        collection_name.insert_one(vlyon_list[k])
    return()


#########################################################################

#####"               Création de la db pour Paris                ########

#########################################################################
def db_create_paris():
    vparis_list=get_vparis()
    dbname=get_database("vélib")
    collection_name=dbname["Paris"]
    for k in range(len(vparis_list)):
        collection_name.insert_one(vparis_list[k])
    return()

#########################################################################


    
if __name__ == "__main__": 
    db_create_lyon()


"""
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