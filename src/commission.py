"""Classe qui gère les commissions"""

from BI import BI

class Commission:

    def __init__(self, pfadresse = ""):
        self.notaireAdresse = pfadresse
        self.commissionNotaire = 456540

    #Renvoie le prix que verse le notaire
    def notairePayeAgence(self):

        #Récupérer le bien en question
        self.commissionNotaire *= 0.07
        print("Le notaire a versé une commission de : " + str(self.commissionNotaire))



if __name__ == "__main__":
    a = Commission()
    b = BI()
    b.ajouterBien("terrain")
    a.notairePayeAgence()