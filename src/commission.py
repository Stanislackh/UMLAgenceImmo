"""Classe qui gère les commissions"""

class Commission:

    def __init__(self, pfadresse = ""):
        self.notaireAdresse = pfadresse
        self.commissionNotaire = False

    #Renvoie le prix que verse le notaire
    def notairePayeAgence(self):

        #Récupérer le bien en question
        self.commissionNotaire = True
        print("Le notaire a versé sa commission")
