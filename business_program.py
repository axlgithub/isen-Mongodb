from Station import Station
import user_program 
import os
import usefull_functions
from pprint import pprint 

#############################################################################

###        find and display a station                                  ######

#############################################################################

def find_station(city):
    db =usefull_functions.get_database("vélib")
    collection= db[city]
    string_to_search=input("\nplease entre the name or partial name you want to search: ")
    string_to_search= string_to_search.upper()
    collection.create_index([('nom',"text")])
    a= collection.find({'$text':{'$search': string_to_search}} )
    for data in a:
        print(data)
    return(a)


#############################################################################

###        update_station                                              ######

#############################################################################

def delete_station(name,city):
    db =usefull_functions.get_database("vélib")
    collection= db[city]
    query={"nom": name}
    collection.delete_one(query)
    return("done")



######################################################################

#############################################################################

###      desactivate_all_stations_in_area                              ######

#############################################################################

def desactivate_all_stations_in_area(city, center_of_desactivation, max_distance):
    list_of_stations_to_desactivate = []
    db =usefull_functions.get_database("vélib")
    collection= db[city]
    collection.create_index([('coordonnees',"2d")])
    a = collection.find(
        {'coordonnees': {'$near': center_of_desactivation, '$maxDistance': max_distance }}
    ) 
    for data in a:
        print("the station "+ data['nom']+" will be desactivated")
        list_of_stations_to_desactivate.append(data['nom'])

    for name in list_of_stations_to_desactivate:
        new_values = {"$set": {'etat': "Hors service"}}
        collection.update_one({'nom': name}, new_values)
    return(0)


######################################################################





#############################################################################

###      average                                                       ######

#############################################################################

def average(a_list_of_stations): #usefull to make the average of the ratio (available bikes/size of the station) for each stations
    new_list = []
    for x in a_list_of_stations:
        size=len(x)
        addition=0
        L = []
        for i in range(1,size):
            addition += x[i]
        average = addition/(size-1)
        L.append(x[0])
        L.append(average)
        new_list.append(L)
    return(new_list)


#############################################################################

###        find and display a station                                  ######

#############################################################################

def stations_ratio_bike():
    print(" this program needs a capture of the data from your city, if you change the city you need to launch the worker program before")
    db =usefull_functions.get_database("vélib")
    collection= db["capture"]
    all_station= collection.find()
    list_Of_All_Station = []
    for x in all_station:
        the_station_already_in_the_list= False
        for station in list_Of_All_Station:
            if station[0]==x['nom']:
                station.append((x['velos_dispo']*100)/x['places_dispo'])
                the_station_already_in_the_list= True
        if the_station_already_in_the_list==False:
            new_station = []
            new_station.append(x['nom'])
            new_station.append((x['velos_dispo']*100)/x['places_dispo'])
            list_Of_All_Station.append(new_station)
    list_station_average= average(list_Of_All_Station)
    for station in list_station_average:
        if station[1]<0.20:
            print("La station "+station[0]+" a un ratio velo/nombre de places moyen sur la capture en dessous de 0.2 avec "+str(station[1]))
    return(0)


######################################################################










if __name__ == "__main__":
    print("Hello, welcome to our Business program.\n")  
    city = usefull_functions.first_launch_from_user()
    os.system("clear")
    print("Welcome to our worker program for the city of",city)
    print("\nWhich action do you want to do ?\nPLEASE SELECT A NUMBER\n")
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
        usefull_functions.update_station(station,city)
    if user_choice =="4":
        tab = 2*[0]
        print("please enter the longitude and latitude of the center point of desactivation: ")
        user_longitude = float(input("\nplease enter your longitude: "))
        user_latitude = float(input("\nplease enter your latitude: "))
        tab[0]=user_longitude
        tab[1]=user_latitude
        user_max_distance = float(input("\nplease enter the distance of the perimeter you want to desactivate (in coordinates not meters): "))
        desactivate_all_stations_in_area(city, tab,user_max_distance)
    if user_choice =="5":
        stations_ratio_bike()
    
    
