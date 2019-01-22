"""Classe Mendat
Attributs :
-
-
-
-
Methodes :
-
-
-
-
-
"""
from BienImmobilier import BienImmobilier

class Mendat:

    def __init__(self,pfduree = 0):
        self.visite = False

    def autorisation(self):
        self.duree = int(input("Entrez le nombre de mois du mendat :"))
        self.visite = True

        #ajouter aux annonces ?
