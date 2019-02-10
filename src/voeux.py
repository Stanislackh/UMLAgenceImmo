"""Classe Voeux"""

from personnes import Personnes
import agence
from mendat import Mendat
import rendezVous

class Voeux:

    #Dictionnaire liste Voeux
    listeVoeux = {}
    keyL = 0

    #Liste des informations client/bien
    infos = []

    def __init__(self,pfprix = 0, pftypebien = "res"):
        self.bienSouhaite = pftypebien
        self.prixSouhaite = pfprix


    def voeuxClient(self,type = "r"):
        #Incremente la clé
        Voeux.keyL += 1

        while (type.lower() != "appartement") and (type.lower() != "maison") and (type.lower() != "terrain"):
            type = input("Type de bien, tapez le type de bien a inscrire : appartement, maison ou terrain : ")

        if type.lower() == "maison":
            self.prixSouhaite = input("Prix souhaité pour le bien : ")
            self.surface = input("Surface au sol souhaité : ")
            self.nbPieces = input("Nombre de pièces souhaité :")

            Voeux.listeVoeux[Voeux.keyL] = type, Personnes.ajouterClient(self), self.prixSouhaite, self.surface, self.nbPieces

        elif type.lower() == "terrain":
            self.prixSouhaite = input("Prix souhaité pour le bien : ")
            self.surface = input("Surface au sol souhaité : ")

            Voeux.listeVoeux[Voeux.keyL] = type, Personnes.ajouterClient(self), self.prixSouhaite, self.surface

        elif type.lower() == "appartement":
            self.prixSouhaite = input("Prix souhaité pour le bien : ")
            self.nbPieces = input("Nombre de pièces souhaité :")

            Voeux.listeVoeux[Voeux.keyL] = type, Personnes.ajouterClient(self), self.prixSouhaite, self.nbPieces

    def checkVoeux(self):
        #Compliqué AF

        #les voeux
        infos = []
        acheteur = ""
        vendeur = ""

        #Parcours de la liste de bien
        for i in agence.Agence.listeBien.values():
            vendeur = i[1][0]

            #Parcours de la liste de voeux par bien proposé
            for j in Voeux.listeVoeux.values():
                acheteur = j[0]

                # Informations client vendeur
                # i[0][0][2]
                # Informations client acheteur
                # j[1][2]

                #Cas de recherche de maison
                if (vendeur == "maison") and (acheteur == "maison"):
                    #vérification pour une maison
                    if vendeur == acheteur:

                        #prix souhaité              Surface souhaité          nombmre de pièces
                        if (i[1][1][1] == j[2]) and (i[1][1][6] == j[3]) and (i[1][1][4] == j[4]):
                            print("Le bien correspond aux recherches")
                            Mendat.autorisation(self)

                            #Ajoute les coordonnées du l'acheteur du vendeur et les infos sur le bien du vendeur
                            Voeux.infos.append(j[1][2])
                            Voeux.infos.append(i[0][0][2])
                            Voeux.infos.append(i[1][1])
                            rendezVous.RendezVous.confirmerVente(self)
                            return Voeux.infos

                        else:
                            print("un critère ne correspond pas")

                #Cas de recherche de terrain
                if (vendeur == "terrain") and (acheteur == "terrain"):

                    #vérification pour un terrain
                    if vendeur == acheteur:

                        #prix souhaité              Surface souhaité
                        if (i[1][1][1] == j[2]) and (i[1][1][4] == j[3]):
                            print("Le bien correspond aux recherches")
                            Mendat.autorisation(self)

                            #Ajoute les coordonnées du l'acheteur du vendeur et les infos sur le bien du vendeur
                            infos.append(j[1][2])
                            infos.append(i[0][0][2])
                            infos.append(i[1][1])
                            rendezVous.RendezVous.confirmerVente(self)
                            return Voeux.infos

                        else:
                            print("un critère ne correspond pas")

                # Cas de recherche d' appartement
                if (vendeur == "appartement") and (acheteur == "appartement"):
                    # vérification pour un terrain
                    if vendeur == acheteur:

                        # prix souhaité              Nombre de pièces souhaité
                        if (i[1][1][1] == j[2]) and (i[1][1][4] == j[3]):
                            print("Le bien correspond aux recherches")
                            Mendat.autorisation(self)

                            #Ajoute les coordonnées du l'acheteur du vendeur et les infos sur le bien du vendeur
                            infos.append(j[1][2])
                            infos.append(i[0][0][2])
                            infos.append(i[1][1])
                            rendezVous.RendezVous.confirmerVente(self)
                            return Voeux.infos

                        else:
                            print("Un critère ne convient pas")


if __name__ == "__main__":
    a = agence.Agence()
    a.inscriptionVendeur()
    b = Voeux()
    b.voeuxClient()
    b.checkVoeux()