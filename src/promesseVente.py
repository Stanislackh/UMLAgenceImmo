"""Classe PromesseVente"""

from voeux import Voeux
import rendezVous

class PromesseVente:

    def __init__(self, pfprixVerse, pfadresseNotaire, pfdateVente, pffraisVente):
        self.prixVerse = pfprixVerse
        self.adresseNotaire = pfadresseNotaire
        self.dateVente = pfdateVente
        self.commission = 0
        self.fraisVente = pffraisVente
        self.signe = False
        self.reste = 0


    def signature(self):

        while (rep.lower() != "oui") and (rep.lower() != "non"):
            rep = input("Voulez vous signer la promesse de vente ? : ")

        if rep == "oui":
            self.signe = True
            print("Promesse de vente signée !")

            self.prixVerse = float(self.infos[2][1]) * 0.1
            print("prix versé au vendeur : " + str(self.prixVerse))

            self.adresseNotaire = input("Entrez l'adresse du notaire : ")

            self.dateVente = self.infos[2][2]
            print("Date vente bien : " + str(self.dateVente))

            self.commission = float(self.infos[2][1]) * 0.07
            print("Commission agence : " + str(self.commission))

            self. reste = float(self.infos[2][1]) - float(self.prixVerse)
            print("Reste à payer : " + str(self.reste))

            self.fraisVente = 0
            
        else:
            self.signe = False
            print("Vente annulée")