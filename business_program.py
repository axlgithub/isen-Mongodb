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
    collection.create_index([('nom',"text")])
    a= collection.find({'$text':{'$search': string_to_search}} )
    for data in a:
        print(data)
    return(a)


######################################################################

#############################################################################

###        update_station                                              ######

#############################################################################

def update_station(name):
    return("to_do")


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
    print("\nEnter 1. Find a station from its name\n 2. Update a station\n 3. Desactivate all the sations in an area\n4. Give all sations with ratio bike under 20%\n")
    user_choice = input("your choice: ")
    if user_choice =="1":
        find_station(city)
    if user_choice =="2":
        update_station()
    if user_choice =="3":
        desactivate_all_stations_in_area()
    if user_choice =="4":
        stations_ratio_bike()
    
    
