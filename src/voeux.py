"""Classe Voeux"""

from personnes import Personnes
from agence import Agence
import mendat

class Voeux:

    #Dictionnaire liste Voeux
    listeVoeux = {}
    keyL = 0

    def __init__(self,pfprix = 0, pftypebien = "res"):
        self.bienSouhaite = pftypebien
        self.prixSouhaite = pfprix


    def voeuxClient(self,type = "r"):
        #Incremente la clé
        Voeux.keyL += 1

        while (type.lower() != "appartement") and (type.lower() != "maison") and (type.lower() != "terrain"):
            type = input("Type de bien, tapez le type de bien a inscrire : appartement, maison ou terrain : ")

        if type.lower() == "maison":

            self.surface = input("Surface au sol souhaité : ")
            self.nbPieces = input("Nombre de pièces souhaité :")

            Voeux.listeVoeux[Voeux.keyL] = Personnes.ajouterClient(self), self.surface, self.nbPieces

        elif type.lower() == "terrain":
            self.surface = input("Surface au sol souhaité : ")

            Voeux.listeVoeux[Voeux.keyL] = Personnes.ajouterClient(self), self.surface

        elif type.lower() == "appartement":
            self.nbPieces = input("Nombre de pièces souhaité :")

            Voeux.listeVoeux[Voeux.keyL] = Personnes.ajouterClient(self), self.nbPieces

    def checkVoeux(self):
        #Compliqué AF
        print("checkVoeux " + str(Agence.listeBien))
        print("checkVoeux 2 : " + str(Voeux.listeVoeux))

    def infoMendat(self):
        #Donne les information sur le bien et fait visiter
        pass

if __name__ == "__main__":
    a = Agence()
    a.inscriptionVendeur()
    b = Voeux()
    b.voeuxClient()
    b.checkVoeux()