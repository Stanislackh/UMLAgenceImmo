
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
        self.orientation = ""
        self.prixDemande = 0
        self.dateVenteSouhait = ""
        self.dateDispo = ""
        self.nombrePieces = 0

    def __str__(self):
        return "" + self.adresse

    def __repr__(self):
        return "" + self.adresse

    def inscrire(self, adresse, orientation, prixDemande, dateVenteSouhait, dateDispo, nombrePieces):
        "permet de créer un bien, de vérifier les paramètres et de l'enregistrer dans les biens inscrit dans l'agence"

        # complet deviandra True quand les données seront validées, permet de boucler avant ça
        complet = False

        # erreurpermet de savoir si il y a eu une itération. Si c'est le cas, on affiche le message d'erreur.
        erreur = False

        while not complet:

            if erreur:
                print("les informations sont incorrectes, veullez réessayer SVP")

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
        self.orientation = orientation
        self.prixDemande = prixDemande
        self.dateVenteSouhait = dateVenteSouhait
        self.dateDispo = dateDispo
        self.nombrePieces = nombrePieces

        # On inscrit le bien dans la liste
        BienImmobilier.listeBien.append(self)

    def afficherTousBiens_adresse(self):
        return BienImmobilier()


"""TESTs"""

b1 = BienImmobilier()
b1.inscrire("loin", "de gauche", "trop", "vite", "maintenant", 1)
print(b1.listeBien)
print(b1.num)

b2 = BienImmobilier()
b2.inscrire("fffffff", "ffffff", "ffff", "fffffff", "ffffff", 2)
print(b2.listeBien)
print(b2.num)

b3 = BienImmobilier()
b3.inscrire("zzzzzzzz", "zzzzzz zzzzzzzz", "zzzzzzz", "zzzzzzzz", "zzzzzzzzz", 1234567)
print(b3.listeBien)
print(b3.num)

print("")

print(str(b3) + " adresse b3")
print(BienImmobilier.listeBien[0].orientation + "  res")