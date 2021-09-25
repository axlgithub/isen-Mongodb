import testWriteInDb
import os 
from bson.son import SON
from pymongo import MongoClient
from pprint import pprint 




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

##############################################################################





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
    db =testWriteInDb.get_database("vélib")
    print("Hello, welcome to our velib application. In which city do you want to make a research ? \n")
    city_of_user = first_launch_from_user()
    collection= db[city_of_user]
   
    os.system("clear")
    print("############################################\n\n\nWelcome to our bike programm for the city of",city_of_user)

    # user location is stored as a tab [longitude, latitude]
    user_localisation = get_user_location()
    closest_location = get_closest_location(collection, user_localisation)
