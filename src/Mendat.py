"""Classe Mendat"""

from rendezVous import RDV

class Mendat:

    def __init__(self, pfduree = 0):
        self.visite = False

    def autorisation(self):
        self.duree = input("Entrez la durée du mendat :")
        self.visite = True

        return self.duree, self.visite