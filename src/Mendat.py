"""Classe Mendat"""

#from BienImmobilier import BienImmobilier
from Personnes import Personnes
from Morale import Morale

class Mendat:

    def __init__(self,pfduree = 0):
        self.visite = False

    def autorisation(self):
        self.duree = int(input("Entrez la durée du mendat :"))
        self.visite = True

        return self.duree, self.visite