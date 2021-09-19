import requests
from pymongo import MongoClient
from pprint import pprint  


##

    ####  Met ton fichier avec en première ligne mot de passe, sur la deuxieme ton login dans le meme dossier que le python dans un ficheir qui s'appelle test2

###


pwdFile = open('test2','r')
pwd=(pwdFile.readline()).strip("\n")
username=(pwdFile.readline()).strip("\n")
pwdFile.close()
print(pwd)
print(username)

CONNECTION_STRING = "mongodb+srv://"+username+":"+pwd+"@cluster0.dragk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
from pymongo import MongoClient
client = MongoClient(CONNECTION_STRING)
conn = MongoClient()
db = conn.test
collection=db.station

premiereStationDepuisPython = {
        "etat":"En service",
        "name":"Première station depuis python",
        "size":12}

collection.insert_one(premiereStationDepuisPython)

"""
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
from pymongo import MongoClient
client = MongoClient(CONNECTION_STRING)

# Create the database for our example (we will use the same database throughout the tutorial
"""