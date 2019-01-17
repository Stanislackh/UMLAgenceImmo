"""Création de l'agence"""

from BienImmobilier import BienImmobilier

class Agence:

    def __init__(self):
        BienImmobilier.__init__(self)


    #Initialise la liste des annonces
    annonce = {}

    #Initialise le compteur de bien
    compt = 0

    #Rentre les information lors du rendez vous
    def encoursRDV(self):
        Agence.annonce[Agence.compt] = BienImmobilier.inscrire(self,"loin", "de gauche", "trop", "vite", "maintenant", 1)
        Agence.compt = Agence.compt + 1
        print(Agence.annonce)

"""Test"""

a = Agence()
a.encoursRDV()
