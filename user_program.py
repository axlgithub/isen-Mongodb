import testWriteInDb

def choice(i):
    user_choice = i.lower()
    if (user_choice == "paris"):
        return (1)
    if (user_choice == "lille"):
        return (2)
    if (user_choice == "lyon"):
        return (3)
    if (user_choice == "rennes1"):
        return (4)
    return(i)

def first_launch_from_user():
    print("Hello, welcome to our velib application. In which city do you want to make a research ? \n")
    while True:
        print("enter the name of the city or one of the number shown bellow\n ")
        print("1.Paris 2.Lille 3.Lyon 4;Rennes\n")
        user_choice = input(":")
        number_of_choice= int(choice(user_choice))
        if ( 1 <= number_of_choice <= 4 ):
            break
        print("please enter a correct city or number")
    print("ok")
    return number_of_choice



if __name__ == "__main__": 
    testWriteInDb.get_database("vélib")
    city_of_user = first_launch_from_user()
    
