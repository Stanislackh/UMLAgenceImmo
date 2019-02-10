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

            Voeux.listeVoeux[Voeux.keyL] = type, Personnes.ajouterClient(self), self.surface, self.nbPieces

        elif type.lower() == "terrain":
            self.surface = input("Surface au sol souhaité : ")

            Voeux.listeVoeux[Voeux.keyL] = type, Personnes.ajouterClient(self), self.surface

        elif type.lower() == "appartement":
            self.nbPieces = input("Nombre de pièces souhaité :")

            Voeux.listeVoeux[Voeux.keyL] = type, Personnes.ajouterClient(self), self.nbPieces

    def checkVoeux(self):
        #Compliqué AF

        #les voeux
        acheteur = ""
        vendeur = ""

        print("checkVoeux " + str(Agence.listeBien))
        print("checkVoeux 2 : " + str(Voeux.listeVoeux))

        for i in Agence.listeBien.values():
            vendeur = i[1][0]
            for j in Voeux.listeVoeux.values():
                acheteur = j[0]

                #Cas de recherche de maison
                if (vendeur == "maison") and (acheteur == "maison"):
                    print("MAISON")
                    #vérification pour une maison
                    if vendeur == acheteur:
                        #prix souhaité
                        if i[1][1][1] == j[2]:
                            print("Prix ok")
                        #nombrede pièces souhaité
                        if i[1][1][4] == j[3]:
                            print("nombre pièces ok")
                            print("Mise en relation")

                #Cas de recherche de terrain
                if (vendeur == "terrain") and (acheteur == "terrain"):
                    print("TERRAIN")
                    #vérification pour un terrain
                    if vendeur == acheteur:
                        #prix souhaité
                        if i[1][1][1] == j[2]:
                            print("Prix ok")
                        #nombrede pièces souhaité
                        if i[1][1][4] == j[2]:
                            print("surface ok")
                            print("Mise en relation")

                # Cas de recherche d' appartement
                if (vendeur == "appartement") and (acheteur == "appartement"):
                    print("APPART")
                    # vérification pour un terrain
                    if vendeur == acheteur:
                        # prix souhaité
                        if i[1][1][1] == j[2]:
                            print("Prix ok")
                        # nombrede pièces souhaité
                        if i[1][1][4] == j[2]:
                            print("nb Pièces ok")
                            print("Mise en relation")


    def infoMendat(self):
        #Donne les information sur le bien et fait visiter
        pass

if __name__ == "__main__":
    a = Agence()
    a.inscriptionVendeur()
    b = Voeux()
    b.voeuxClient()
    b.checkVoeux()