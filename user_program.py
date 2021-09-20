import testWriteInDb
import os 



#############################################################################

###          choice of the city                                         ######

#############################################################################


def choice(i):
    user_choice = i
    if (int(user_choice) == 1):
        return ("paris")
    if (int(user_choice) == 2):
        return ("lille")
    if (int(user_choice) == 3):
        return ("lyon")
    if (int(user_choice) == 4):
        return ("rennes")
    user_choice = user_choice.lower()
    return(user_choice)

##############################################################################





#############################################################################

### first_launch_from_user first message and interactions with the user #####

#############################################################################

def first_launch_from_user():
    print("Hello, welcome to our velib application. In which city do you want to make a research ? \n")
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
    L = []
    user_longitude = input("\nplease enter your longitude: ")
    user_latitude = input("\nplease enter your latitude: ")
    return L[user_longitude,user_latitude]

#############################################################################





#############################################################################

### get_closest_location make a request to find closest station         #####

#############################################################################

def get_closest_location(city, location_of_user):
    return 1

#############################################################################




if __name__ == "__main__": 
    testWriteInDb.get_database("vélib")
    city_of_user = first_launch_from_user()

   
    os.system("clear")
    print("\n\n\n############################################\n\n\nWelcome to our bike programm for the city of",city_of_user)

    # user location is stored as a list [longitude, latitude]
    user_localisation = get_user_location()

    print("the closest station is: ")
    closest_location = get_closest_location(city_of_user, user_localisation)
