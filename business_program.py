from Station import Station
import user_program 
import os
import testWriteInDb
from pprint import pprint 

#############################################################################

###        find and display a station                                  ######

#############################################################################

def find_station(city):
    db =testWriteInDb.get_database("vélib")
    collection= db[city]
    string_to_search=input("\nplease entre the name or partial name you want to search: ")
    string_to_search= string_to_search.upper()
    a= collection.find( {'nom': "BOULEVARD DE VALMY"} )
    for data in a:
        print(data)
    print(a)
    print("okok")
    return("to_do")


######################################################################

#############################################################################

###        update_station                                              ######

#############################################################################

def update_station(name,city):
    db =testWriteInDb.get_database("vélib")
    collection= db[city]
    query={"nom": name}
    if city =="Lille":
        new_data = testWriteInDb.get_vlille()
        for x in new_data:
            if x["fields"]["nom"] == name: 
                number_of_available_places = x["fields"]["nbplacesdispo"]
                number_of_bikes_availables = x["fields"]["nbvelosdispo"]
                etat=x["fields"]["etat"]
                new_values1 = {"$set": {'places_dispo': number_of_available_places}}
                new_values2 = {"$set": {'velos_dispo': number_of_bikes_availables}}
                new_values3= {"$set": {'etat': etat}}
                collection.update_one({'nom': name}, new_values1)
                collection.update_one({'nom': name}, new_values2)
                collection.update_one({'nom': name}, new_values3)
    if city =="Rennes":
        new_data = testWriteInDb.get_vrennes()
        for x in new_data:
            if x["fields"]["nom"] == name: 
                number_of_available_places = x["fields"]["nbplacesdispo"]
                number_of_bikes_availables = x["fields"]["nbvelosdispo"]
                etat=x["fields"]["etat"]
                new_values1 = {"$set": {'places_dispo': number_of_available_places}}
                new_values2 = {"$set": {'velos_dispo': number_of_bikes_availables}}
                new_values3= {"$set": {'etat': etat}}
                collection.update_one({'nom': name}, new_values1)
                collection.update_one({'nom': name}, new_values2)
                collection.update_one({'nom': name}, new_values3)
    if city =="Paris":
        new_data = testWriteInDb.get_vparis()
        for x in new_data:
            if x["fields"]["name"] == name: 
                number_of_available_places = x["fields"]["nbplacesdispo"]
                number_of_bikes_availables = x["fields"]["nbvelosdispo"]
                etat=x["fields"]["is_renting"]
                new_values1 = {"$set": {'places_dispo': number_of_available_places}}
                new_values2 = {"$set": {'velos_dispo': number_of_bikes_availables}}
                new_values3= {"$set": {'etat': etat}}
                collection.update_one({'nom': name}, new_values1)
                collection.update_one({'nom': name}, new_values2)
                collection.update_one({'nom': name}, new_values3)
    if city =="Lyon":
        print("to be done")
    return("done")

#############################################################################

###        update_station                                              ######

#############################################################################

def delete_station(name,city):
    db =testWriteInDb.get_database("vélib")
    collection= db[city]
    query={"nom": name}
    collection.delete_one(query)
    return("done")



######################################################################

#############################################################################

###      desactivate_all_stations_in_area                              ######

#############################################################################

def desactivate_all_stations_in_area(name):
    return("to_do")


######################################################################

#############################################################################

###        find and display a station                                  ######

#############################################################################

def stations_ratio_bike(name):
    return("to_do")


######################################################################

if __name__ == "__main__":
    print("Hello, welcome to our Business program.\n")  
    city = user_program.first_launch_from_user()
    os.system("clear")
    print("Welcome to our worker program for the city of",city)
    print("\nWhich action do you want to do ?\n")
    print("\nEnter 1. Find a station from its name\n2. Delete a station\n3. Update a station \n4. Desactivate all the sations in an area\n5. Give all sations with ratio bike under 20%\n")
    user_choice = input("your choice: ")
    if user_choice =="1":
        find_station(city)
    if user_choice =="2":
        station=input("\nPlease enter the name of the station you want to delete: ")
        station= station.upper()
        delete_station(station,city)
    if user_choice=="3":
        station=input("\nPlease enter the name of the station you want to update: ")
        station= station.upper()
        update_station(station,city)
    if user_choice =="4":
        desactivate_all_stations_in_area()
    if user_choice =="5":
        stations_ratio_bike()
    
    
