import requests
from pprint import pprint  


#############################################################################

###        get_database, from https://www.mongodb.com/languages/python ######

#############################################################################

def get_database(name_of_data_base):
    from pymongo import MongoClient
    import pymongo

    #Get the password and the username in a file next to this python script 
    pwd_file = open('test2','r')
    pwd=(pwd_file.readline()).strip("\n")
    username=(pwd_file.readline()).strip("\n")
    pwd_file.close()

    #Fabrication of the connection string used to connect ourselves with our password and login to the database
    CONNECTION_STRING = "mongodb+srv://"+username+":"+pwd+"@cluster0.dragk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)

    #return the database asked in parameter
    return client[name_of_data_base]

#################################





#############################################################################

###        new_station                                                 ######

#############################################################################

def new_station(state,name,size):
    new_station = {
        {
        "state": state,
        "name": name,
        "size": size}  
    }









if __name__ == "__main__":  
    station = new_station("En service", "rue nationale", 10)
    # Get the database
    dbname = get_database("test")
    print(dbname)
    collection_name= dbname["station"]
    collection_name.insert_one(station)