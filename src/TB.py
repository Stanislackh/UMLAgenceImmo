from BI import BI
import re

class Terrain(BI):

    genre = "terrain"

    def __init__(self, pfnum, pfsuperficie, pfadresse, pfprixDemande, pfdateVenteSouhait, pfdateDispo):
        BI.__init__(self, pfnum, pfadresse, pfprixDemande, pfdateVenteSouhait, pfdateDispo)
        self.superficie = pfsuperficie


    def inscrireTerrain(self):

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

        BI.ajouterBien(self)
        self.superficie = input("Superficie : ")

        return self.adresse, self.prixDemande, self.dateVenteSouhait, self.dateDispo, self.superficie

class Maison(BI):

    genre = "maison"

    def __init__(self, pfnum, pfnombrePieces, pforientation, pfadresse, pfprixDemande, pfdateVenteSouhait, pfdateDispo, pfSurface):
        BI.__init__(self, pfnum, pfadresse, pfprixDemande, pfdateVenteSouhait, pfdateDispo)
        self.surfaceHabitable = pfSurface
        self.nombrePieces = pfnombrePieces
        self.orientation = pforientation

    def inscrireMaison(self):

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

        BI.ajouterBien(self)
        self.surfaceHabitable = input("Surface habitable : ")
        self.nombrePieces = input("nombre de pièces : ")
        self.orientation = input("Orientation de la maison : ")

        return self.adresse, self.prixDemande, self.dateVenteSouhait, self.dateDispo, self.nombrePieces, self.orientation, self.surfaceHabitable

class Appart(BI):

    genre = "appartement"

    def __init__(self, pfnum, pfadresse, pfprixDemande, pfdateVenteSouhait, pfdateDispo, pfnbPiece, pfetage, pfcharges):
        BI.__init__(self, pfnum, pfadresse, pfprixDemande, pfdateVenteSouhait, pfdateDispo)
        self.nombrePieces = pfnbPiece
        self.etage = pfetage
        self.charges = pfcharges

    def inscrireAppart(self):

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

        BI.ajouterBien(self)
        self.nombrePieces = input("Nombre de pièces : ")
        self.etage = input("nombre d'étages : ")
        self.charges = input("charges : ")


        return self.adresse, self.prixDemande, self.dateVenteSouhait, self.dateDispo, self.nombrePieces, self.etage, self.charges
