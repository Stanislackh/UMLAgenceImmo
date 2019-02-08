from BI import BienImmobilier
import BI
import re


class Terrain(BienImmobilier):

    def __init__(self):
        BienImmobilier.__init__(self)
        self.superficie = 0

    def inscrireTerrain(self, superficie, adresse, prixDemande, dateVenteSouhait, dateDispo):

        # complet deviandra True quand les données seront validées, permet de boucler avant ça
        complet = False

        # erreurpermet de savoir si il y a eu une itération. Si c'est le cas, on affiche le message d'erreur.
        erreur = False

        while not complet:

            if erreur:
                print("les informations sont incorrectes, veuillez réessayer SVP")

                # A FAIRE : vérifier la conformité des infos

            # complet passe à True si les données sont validées
            complet = True
            # erreur passe à True quoi qu'il arrive
            erreur = True

        self.superficie = superficie

        BienImmobilier.inscrire(self, adresse, prixDemande, dateVenteSouhait, dateDispo)
        BI.BienImmobilier.listeBien[self.num] = self

class Maison(BienImmobilier):

    def __init__(self):
        BienImmobilier.__init__(self)
        self.nombrePieces = 0
        self.orientation = ""

    def inscrireMaison(self, nombrePieces, orientation, adresse, prixDemande, dateVenteSouhait, dateDispo):

        # complet deviandra True quand les données seront validées, permet de boucler avant ça
        complet = False

        # erreurpermet de savoir si il y a eu une itération. Si c'est le cas, on affiche le message d'erreur.
        erreur = False

        while not complet:

            if erreur:
                print("les informations sont incorrectes, veuillez réessayer SVP")

                # A FAIRE : vérifier la conformité des infos

            # complet passe à True si les données sont validées
            complet = True
            # erreur passe à True quoi qu'il arrive
            erreur = True

        self.nombrePieces = nombrePieces
        self.orientation = orientation

        BienImmobilier.inscrire(self, adresse, prixDemande, dateVenteSouhait, dateDispo)
        BI.appendListe(self, self.num)

class Appart(BienImmobilier):

    def __init__(self):
        BienImmobilier.__init__(self)
        self.nombrePieces = 0
        self.etage = 0
        self.charges = 0

    def inscrireAppart(self, nombrePieces, etage, charges, adresse, prixDemande, dateVenteSouhait, dateDispo):

        # complet deviandra True quand les données seront validées, permet de boucler avant ça
        complet = False

        # erreurpermet de savoir si il y a eu une itération. Si c'est le cas, on affiche le message d'erreur.
        erreur = False

        while not complet:

            if erreur:
                print("les informations sont incorrectes, veuillez réessayer SVP")

                # A FAIRE : vérifier la conformité des infos

            # complet passe à True si les données sont validées
            complet = True
            # erreur passe à True quoi qu'il arrive
            erreur = True

        self.nombrePieces = nombrePieces
        self.etage = etage
        self.charges = charges

        BienImmobilier.inscrire(self, adresse, prixDemande, dateVenteSouhait, dateDispo)
        BI.appendListe(self, self.num)