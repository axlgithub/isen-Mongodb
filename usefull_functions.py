from Station import Station
from pprint import pprint  
import time
import get_self_services_bicycle
from pymongo import MongoClient


#############################################################################

###  Importe la database depuis le cloud en python (nécessite un mot de passe et un nom d'utilisateur ######

#############################################################################

def get_database(name_of_data_base):
    #Get the password and the username in a file next to this python script 
    pwd_file = open('credentials','r')
    pwd=(pwd_file.readline()).strip("\n")
    username=(pwd_file.readline()).strip("\n")
    pwd_file.close()

    #Fabrication of the connection string used to connect ourselves with our password and login to the database
    CONNECTION_STRING = "mongodb+srv://"+username+":"+pwd+"@cluster0.dragk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)

    #return the database asked in parameter
    return client[name_of_data_base]


#############################################################################

###        capture                                                     ######

#############################################################################

def capture(city):
    if city == "Paris":
        new_data = get_self_services_bicycle.get_vparis()
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
        new_data = get_self_services_bicycle.get_vlille()
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
        new_data = get_self_services_bicycle.get_vlyon()
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
        new_data = get_self_services_bicycle.get_vrennes()
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

#############################################################################

###        update_station                                              ######

#############################################################################

def update_station(name,city):
    db =get_self_services_bicycle.get_database("vélib")
    collection= db[city]
    if city =="Lille":
        new_data = get_self_services_bicycle.get_vlille()
        for x in new_data:
            if x["fields"]["nom"] == name: 
                number_of_available_places = x["fields"]["nbplacesdispo"]-x["fields"]["nbvelosdispo"]
                number_of_bikes_availables = x["fields"]["nbvelosdispo"]
                etat=x["fields"]["etat"]
                new_values1 = {"$set": {'places_dispo': number_of_available_places}}
                new_values2 = {"$set": {'velos_dispo': number_of_bikes_availables}}
                new_values3= {"$set": {'etat': etat}}
                collection.update_one({'nom': name}, new_values1)
                collection.update_one({'nom': name}, new_values2)
                collection.update_one({'nom': name}, new_values3)
                return(0)
    if city =="Rennes":
        new_data = get_self_services_bicycle.get_vrennes()
        for x in new_data:
            if x["fields"]["nom"] == name: 
                number_of_available_places = x["fields"]["nombreemplacementsdisponibles"]
                number_of_bikes_availables = x["fields"]["nbvelosdispo"]
                etat=x["fields"]["etat"]
                new_values1 = {"$set": {'places_dispo': number_of_available_places}}
                new_values2 = {"$set": {'velos_dispo': number_of_bikes_availables}}
                new_values3= {"$set": {'etat': etat}}
                collection.update_one({'nom': name}, new_values1)
                collection.update_one({'nom': name}, new_values2)
                collection.update_one({'nom': name}, new_values3)
                return(0)
    if city =="Paris":
        new_data = get_self_services_bicycle.get_vparis()
        for x in new_data:
            if x["fields"]["name"] == name: 
                number_of_available_places = x["fields"]["numdocksavailable"]
                number_of_bikes_availables = x["fields"]["numbikesavailable"]
                etat=x["fields"]["is_renting"]
                new_values1 = {"$set": {'places_dispo': number_of_available_places}}
                new_values2 = {"$set": {'velos_dispo': number_of_bikes_availables}}
                new_values3= {"$set": {'etat': etat}}
                collection.update_one({'nom': name}, new_values1)
                collection.update_one({'nom': name}, new_values2)
                collection.update_one({'nom': name}, new_values3)
                return(0)
    if city =="Lyon":
        new_data = get_self_services_bicycle.get_vlyon()
        for x in new_data:
            if x["name"] == name: 
                number_of_available_places = x["empty_slots"]
                number_of_bikes_availables = x["free_bikes"]
                etat=x["extra"]["status"]
                new_values1 = {"$set": {'places_dispo': number_of_available_places}}
                new_values2 = {"$set": {'velos_dispo': number_of_bikes_availables}}
                new_values3= {"$set": {'etat': etat}}
                collection.update_one({'nom': name}, new_values1)
                collection.update_one({'nom': name}, new_values2)
                collection.update_one({'nom': name}, new_values3)
    return("done")


#############################################################################

###        update                                                      ######

#############################################################################

def update(city):
    if city == "Paris":
        new_data = get_self_services_bicycle.get_vparis()
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
        new_data = get_self_services_bicycle.get_vlille()
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
        new_data = get_self_services_bicycle.get_vlyon()
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
        new_data = get_self_services_bicycle.get_vrennes()
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
         

#############################################################################

###        clear                                                       ######

#############################################################################

def clear(collection_name):
    dbname=get_database("vélib")
    collection = dbname[collection_name]
    collection.drop()

#############################################################################

###          choice of the city                                         ######

#############################################################################


def choice(i):
    user_choice = i
    if (user_choice == "1"):
        return ("paris")
    if (user_choice == "2"):
        return ("lille")
    if (user_choice == "3"):
        return ("lyon")
    if (user_choice == "4"):
        return ("rennes")
    user_choice = user_choice.lower()
    return(user_choice)


#############################################################################

### first_launch_from_user first message and interactions with the user #####

#############################################################################

def first_launch_from_user():
    while True:
        print("enter the name of the city or one of the number shown bellow\n ")
        print("1.Paris 2.Lille 3.Lyon 4;Rennes\n")
        user_choice = input(":")
        city_of_user= choice(user_choice)
        if ( city_of_user == "lille" or city_of_user == "lyon" or city_of_user == "paris" or city_of_user == "rennes"):
            break
        print("please enter a correct city or number")
    return (city_of_user.capitalize())

##############################################################################
