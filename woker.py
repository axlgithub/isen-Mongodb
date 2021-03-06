import usefull_functions
import os 
import time


#############################################################################

###      capture_and_update_data_of_city                               ######

#############################################################################


def capture_and_update_data_of_city(city):
    usefull_functions.capture(city)
    usefull_functions.update(city)
    print("ok")

    
#############################################################################

###          run timed loop                                            ######

#############################################################################


def timed_worker(time_in_seconds,city):
    t=0
    initial_time=time.time()
    usefull_functions.clear("capture")
    while (t<time_in_seconds):
        one_minute_chrono = time.time()
        capture_and_update_data_of_city(city)
        time.sleep(60.0 - ((time.time() - one_minute_chrono) % 60.0))
        t=time.time()-initial_time
        print(time_in_seconds-t," seconds to go")
        os.system("clear")

    

##############################################################################

if __name__ == "__main__": 
    print("Hello, welcome to our worker program.\n")
    city = usefull_functions.first_launch_from_user()
    os.system("clear")
    print("Welcome to our worker program for the city of",city)
    print("\nThis program will take some time, please wait, if you think you have enough data you can stop it with the keyboard\n")
    timed_worker(3600,city)
    