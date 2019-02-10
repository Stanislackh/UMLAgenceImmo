"""Classe PromesseVente"""

from voeux import Voeux
import commission
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
        self.retraitAcheteur = False
        self.pret = False


    def signature(self):

        rep = "r"
        while (rep.lower() != "oui") and (rep.lower() != "non"):
            rep = input("Voulez vous signer la promesse de vente ? : ")

        if rep == "oui":
            print("Le vendeur ne peut plus se dérire !")

            gre = 'r'
            while (gre.lower() != "oui") and (gre.lower() != "non"):
                gre = input("Attendez vous un prêt bancaire ? : ")

                if gre.lower() == "oui":
                    self.pret = True

            self.signe = True
            print("Promesse de vente signée !")

            self.prixVerse = float(self.infos[2][1]) * float(0.1)
            print("prix versé au vendeur : " + str(self.prixVerse))

            self.adresseNotaire = input("Entrez l'adresse du notaire : ")

            self.dateVente = self.infos[2][2]
            print("Date vente bien : " + str(self.dateVente))

            self.commission = float(self.infos[2][1]) * float(0.07)
            print("Commission agence : " + str(self.commission))

            self. reste = float(self.infos[2][1]) - float(self.prixVerse)
            print("Reste à payer : " + str(self.reste))

            self.fraisVente = 0

            tre = 'r'
            while (tre.lower() != "oui") and (tre.lower() != "non"):
                tre = input("Voulez vous finaliser l'achat ? : ")

            if tre.lower() == "oui":
                if self.pret == False:
                    self.retraitAcheteur = False
                    commission.Commission.notairePayeAgence(self)
                    print("Achat effectué!")

                elif self.pret == True:
                    self.retraitAcheteur = False
                    commission.Commission.notairePayeAgence(self)
                    print("Achat effectué !")

            if tre.lower() == "non":
                if self.pret == True:
                    self.retraitAcheteur = True
                    print("Achat annulé ! Acheteur remboursé !")

                elif self.pret == False:
                    self.retraitAcheteur = True
                    print("Achat annulé ! le vendeur garde l'avance")

        else:
            self.signe = False
            print("Vente annulée")