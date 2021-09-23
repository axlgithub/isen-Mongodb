## Comme MongoDb nous pouvons stocker presque tout dans une base de données MongoDb nous avons penser à stocker un
## objet station. Cependant, mongodb ne peut pas faire le mapping de l'objet sur un document. Nous avons tout de
## même conservé la classe afin de se servir du constructeur.
class Station:
    def __init__(self,_id,etat,velos_dispo,places_dispo,nom,latitude,longitude):
        self._id=_id
        self.etat=etat
        self.velos_dispo=velos_dispo
        self.places_dispo=places_dispo
        self.nom=nom
        self.coordonnees=[latitude,longitude]

    def print(self):
        return(self.nom)
