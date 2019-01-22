"""Création de l'agence"""

from BienImmobilier import BienImmobilier
from Personnes import Personnes
from RDV import RDV

class Agence:

    def __init__(self):
        pass


    #Initialisation des types de personnes
    vendeur ={}
    acheteur = {}
    keyA = 0
    keyV = 0

    #Inscrit un vendeur
    def inscriptionVendeur(self):

        #Incrémente la clé vendeur
        Agence.keyA += 1
        #Ajoute le client au dictionnaire
        Agence.vendeur[Agence.keyA] = Personnes.ajouterVendeurPhysique(self)

        #Prise de RendezVous pour le mandat
        RDV.PrendreRDV()

    #Initialise la liste des annonces
    annonce = {}

    #Initialise le compteur de bien
    compt = 0

    #Rentre les information lors du rendez vous
    def encoursRDV(self):
        Agence.annonce[Agence.compt] = BienImmobilier.inscrire(self,"loin", "de gauche", "trop", "vite", "maintenant", 1)
        Agence.compt = Agence.compt + 1
        print(Agence.annonce)


    def __str__(self):
        return str(Agence.vendeur)
"""Test"""

a = Agence()
a.inscriptionVendeur()
print(a)
