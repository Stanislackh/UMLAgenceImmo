from .TypeBienImmo import Terrain
from .TypeBienImmo import Maison
from .TypeBienImmo import Appart

class BienImmobilier:
    "classe definissant les biens immobiliers"

    # identifiant unique incrémenté à chaque instanciation
    num = 1

    # Liste des biens inscrits
    listeBien = []

    def __init__(self):
        "Un bien a un identifiant unique, une adresse, une orientation, un prix demandé, un date de vente souhaitée, une disponibilité, et un nombre de pièces = 0 si il s'agit d'un terrain"
        self.num = 0
        self.adresse = ""
        self.prixDemande = 0
        self.dateVenteSouhait = ""
        self.dateDispo = ""

    def __str__(self):
        return "bien immobilier n°" + str(self.num) + " adresse: " + self.adresse

    def __repr__(self):
        return "" + self.adresse

    def inscrire(self, adresse, prixDemande, dateVenteSouhait, dateDispo):
        "permet de créer un bien, de vérifier les paramètres et de l'enregistrer dans les biens inscrit dans l'agence"

        # complet deviandra True quand les données seront validées, permet de boucler avant ça
        complet = False

        # erreurpermet de savoir si il y a eu une itération. Si c'est le cas, on affiche le message d'erreur.
        erreur = False

        while not complet:

            if erreur:
                return print("les informations sont incorrectes, veuillez réessayer SVP")

                # A FAIRE : vérifier la conformité des infos

            # complet passe à True si les données sont validées
            complet = True
            # erreur passe à True quoi qu'il arrive
            erreur = True

        # on incrémente la varible de classe identifiant et on l'affecte à l'identifiant de l'objet
        self.num = BienImmobilier.num
        BienImmobilier.num = BienImmobilier.num + 1

        # On affecte
        self.adresse = adresse
        self.prixDemande = prixDemande
        self.dateVenteSouhait = dateVenteSouhait
        self.dateDispo = dateDispo

    def inscription(self, typeBien):

        if typeBien.lower() == "terrain":
            adresse = input("adresse")
            prixDemande = input("prix demandé")
            dateVenteSouhait = input("date de vente souhaité")
            dateDispo = input("date de disponibilité")
            superficie = input("superficie")

            Terrain.inscrireTerrain(superficie, adresse, prixDemande, dateVenteSouhait, dateDispo)

        elif typeBien.lower() == "maison":
            adresse = input("adresse")
            prixDemande = input("prix demandé")
            dateVenteSouhait = input("date de vente souhaité")
            dateDispo = input("date de disponibilité")
            superficie = input("superficie")

            Maison.inscrireTerrain(superficie, adresse, prixDemande, dateVenteSouhait, dateDispo)

        elif typeBien.lower() == "appartement":

            adresse = input("adresse")
            prixDemande = input("prix demandé")
            dateVenteSouhait = input("date de vente souhaité")
            dateDispo = input("date de disponibilité")
            superficie = input("superficie")

            Appart.inscrireTerrain(superficie, adresse, prixDemande, dateVenteSouhait, dateDispo)

    def afficherTousBiens_adresse(self):
        return BienImmobilier()


"""TESTs"""
"""
b1 = BienImmobilier()
b1.inscrire("loin", "de gauche", "trop", "vite", "maintenant", 1)
print(b1.listeBien)
print(b1.num)
b1 = BienImmobilier()
b1.inscrire("loin", "de gauche", "trop", "vite", "maintenant")
print(b1.listeBien)
print(b1.num) 
print(BienImmobilier.listeBien[0].orientation + "  res")"""

