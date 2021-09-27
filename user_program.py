import usefull_functions
import os 
from pymongo import MongoClient


#############################################################################

### get_user_location ask longitude and latitude and returns a list     #####

#############################################################################

def get_user_location():
    tab = 2*[0]
    user_longitude = float(input("\nplease enter your longitude: "))
    user_latitude = float(input("\nplease enter your latitude: "))
    tab[0]=user_longitude
    tab[1]=user_latitude
    return tab

#############################################################################





#############################################################################

### get_closest_location make a request to find closest station         #####

#############################################################################

def get_closest_location(collection, location_of_user):
    max_distance= 0.01
    collection.create_index([('coordonnees',"2d")])

    # Si l'on souhaite ne plus avoir seulement la station la plus proche il suffit de modifier le find_one en find 
    a = collection.find_one(
        {'coordonnees': {'$near': location_of_user, '$maxDistance': max_distance }}
    ) 
    name_of_closest_station = a['nom']
    number_of_available_bikes=a['velos_dispo']
    number_of_free_places=a['places_dispo']
    print('La station la plus proches est '+name_of_closest_station+'. Il reste '+str(number_of_available_bikes)+' velos de disponibles et '+str(number_of_free_places)+' places de libres')
    return(0)

    
    

#############################################################################




if __name__ == "__main__": 
    db =usefull_functions.get_database("vélib")
    print("Hello, welcome to our velib application. In which city do you want to make a research ? \n")
    city_of_user = usefull_functions.first_launch_from_user()
    collection= db[city_of_user]
   
    os.system("clear")
    print("############################################\n\n\nWelcome to our bike programm for the city of",city_of_user)

    # user location is stored as a tab [longitude, latitude]
    user_localisation = get_user_location()
    closest_location = get_closest_location(collection, user_localisation)
