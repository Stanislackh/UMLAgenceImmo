"""Définition de la classe de BienImmobilier avec les attributs suivants:
    - id()
    ect...

    """


"""Classe Bien immobilier 
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

class BienImmobilier:

    num = 1

    def __init__(self, adresse, orientation, prixDemande, dateVenteSouhait, dateDispo, nombrePieces):
        self.id = self.num
        self.adresse
        self.orientation
        self.prixDemande
        self.dateVenteSouhait
        self.dateDispo
        self.nombrePieces
        self.num += 1

    """
    def AjoutBien(self, adresse, orientation, prixDemande, dateVenteSouhait, dateDispo, nombre, nombrePieces):

    complet = False
    while complet == False:
        adresse = input("entrer l'adresse du bien : ")
        adresse = input("entrer l'orientation du bien : ")
        adresse = input("entrer le prix demandé du bien : ")
        adresse = input("entrer la date de vente souhaité : ")
        adresse = input("entrer la date de disponnibilité du bien : ")
        adresse = input("entrer le nombre de pièces du bien : ")
        
        # vérifier la conformité des infos
        
        complet = True

        """

    hh