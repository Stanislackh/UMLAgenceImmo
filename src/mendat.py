"""Classe Mendat"""

class Mendat():

    def __init__(self, pfduree = 0):
        self.visite = False

    def duree(self):
        self.duree = input("Entrez la durée du mendat :")
        return self.duree

    def autorisation(self):
        self.visite = True
        print("visite = " + str(self.visite))
        return self.visite
