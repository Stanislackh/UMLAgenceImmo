"""Classe Voeux"""


class Voeux:
    "classe définissant les attentes d'un acheteur envers les paramètres des biens"

    # liste des voeux
    listeVoeux = {}

    def __init__(self):

        # id du voeu est celui de l'acheteur, qui est donc forcément unique.
        self.num

        # type de bien voulu
        self.type

        # parametres voulus
        self.localisation
        self.prix
        self.disponnibilite
        self.superficie
        self.nombrePieces
        self.orientation
        self.charges
        self.etage


