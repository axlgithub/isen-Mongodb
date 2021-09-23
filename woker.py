import testWriteInDb
import os 
from bson.son import SON
from pymongo import MongoClient
import sched
import time
import user_program





#############################################################################

###      capture_and_update_data_of_city                               ######

#############################################################################


def capture_and_update_data_of_city(city):
    user_program.update(city)
    print("ok")

    

##############################################################################








#############################################################################

###          run timed loop                                            ######

#############################################################################


def timed_worker(time_in_seconds,city):
    t=0
    initial_time=time.time()
    while (t<time_in_seconds):
        one_minute_chrono = time.time()
        capture_and_update_data_of_city(city)
        time.sleep(60.0 - ((time.time() - one_minute_chrono) % 60.0))
        t=time.time()-initial_time
        print(time_in_seconds-t," seconds to go")

    

##############################################################################

if __name__ == "__main__": 
    print("Hello, welcome to our worker program.\n")
    city = user_program.first_launch_from_user()
    os.system("clear")
    print("Welcome to our worker program for the city of",city)
    timed_worker(3600,city)
    