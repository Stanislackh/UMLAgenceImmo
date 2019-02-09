"""Classe PromesseVente"""


class PromesseVente:

    def __init__(self, pfprixVerse, pfadresseNotaire, pfdateVente, pfprixBien, pffraisVente):
        self.prixVerse = pfprixVerse
        self.adresseNotaire = pfadresseNotaire
        self.dateVente = pfdateVente
        self.commission = (pfprixBien * 0.07)
        self.fraisVente = pffraisVente


    def confirmerVente(self):

        #L'acheteur verse 10% du prix
        Agence.vendeur
