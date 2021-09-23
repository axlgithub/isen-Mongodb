import testWriteInDb
import os 
from bson.son import SON
from pymongo import MongoClient




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
    """
    collection.create_index([('geometry.coordinates', '2dsphere')])
    closest_station = ( collection.find_one({
    "location": {
        "$nearSphere": {
            "$geometry": {
                "type": "Point",
                "coordinates": location_of_user
            },
            "$maxDistance": 10000000000000000
        }
    }
}))
"""
    max_distance= 10000000000
    query = {
    "geolocations": SON([("$near", [location_of_user[1], location_of_user[0]]), ("$maxDistance", 0.01)])
}
    for doc in collection.find(query):
        print(doc)
    return 1

"""
    for x in collection.find({},{ "nom": "RUE ROYALE "}):
        result=x
        print(x) 
    return (x)
"""

    
    

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

    print("the closest station is: ")
    closest_location = get_closest_location(collection, user_localisation)
