"""Création de l'agence"""

#from BienImmobilier import BienImmobilier
from personnes import Personnes
from morale import Morale
from BI import BI
import TB
from rendezVous import RendezVous

class Agence:

    def __init__(self):
        pass

    #Initialisation des types de personnes
    vendeur ={}
    keyV = 0
    acheteur = {}
    keyA = 0
    #liste des biens
    listeBien = {}
    keyB = 0

    #Inscrit un vendeur
    def inscriptionVendeur(self, type= "r"):

        while (type != "physique") and (type != "morale"):
            type = input("Tapez physique pour inscrire une personne ou morale pour une entreprise : ")

            #Vendeur Physique
            if type.lower() == "physique":

                #Incrémente la clé vendeur
                Agence.keyV += 1
                #Ajoute le vendeur au dictionnaire et ajoute la durée du mendat
                Agence.vendeur[Agence.keyV] = Personnes.ajouterClient(self), Personnes.ajouterMendat(self)
                Agence.listeBien[Agence.keyB] = Agence.vendeur[Agence.keyV], RendezVous.prendreRDV(self)

            #Vendeur Morale
            elif type.lower() == "morale":

                #Incrémente la clé vendeur
                Agence.keyV += 1
                #Ajoute le vendeur au dicotionnaire et ajoute la durée du mendat
                Agence.vendeur[Agence.keyV] = Morale.ajouterPersonneMorale(self)
                Agence.listeBien[Agence.keyB] = Agence.vendeur[Agence.keyV], RendezVous.prendreRDV(self)

    #Initialise la liste des annonces
    annonce = {}

    #Initialise le compteur de bien
    compt = 0

    #Inscrit un Acheteur potentiel
    def inscriptionAcheteur(self, type = "r"):

        #Incrémente les acheteur
        Agence.keyA += 1

        while (type != "physique") and (type != "morale"):
            type = input("Tapez physique pour inscrire une personne ou morale pour une entreprise : ")

            #Vendeur Physique
            if type.lower() == "physique":
                #Ajoute le vendeur au dictionnaire
                Agence.acheteur[Agence.keyA] = Personnes.ajouterClient(self)

            #Vendeur Morale
            elif type.lower() == "morale":
                #Ajoute le vendeur au dicotionnaire
                Agence.acheteur[Agence.keyA] = Morale.ajouterPersonneMorale(self)

    #Rentre les information lors du rendez vous
    # def encoursRDV(self):
    #     Agence.annonce[Agence.compt] = BienImmobilier.inscrire(self,"loin", "de gauche", "trop", "vite", "maintenant", 1)
    #     Agence.compt = Agence.compt + 1
    #     print(Agence.annonce)


    def __str__(self):
        return str(Agence.vendeur)


"""Test"""

a = Agence()
a.inscriptionVendeur()
print(a.vendeur)

print(a.listeBien)
