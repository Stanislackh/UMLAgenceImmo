"""Classe Mendat"""

from rendezVous import RDV

class Mendat:

    def __init__(self, pfduree = 0):
        self.visite = False

    def autorisation(self):
        self.duree = input("Entrez la durée du mendat :")
        self.visite = True

    def inscrireMandat(self):

        #complet deviandra True quand les données seront validées, permet de boucler avant ça
        complet = False


        erreur = False

        while not complet:

            if erreur:
                print("les informations sont incorrectes, veullez réessayer SVP")

                # A FAIRE : vérifier la conformité des infos: 1 propriétaire et 1 bien immobilier non possédé

            # complet passe à True si les données sont validées
            complet = True
            # erreur passe à True
            erreur = True


