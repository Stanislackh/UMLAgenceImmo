

class BienImmobilier:

    #identifiant unique incrémenté à chaque instanciation
    num = 1

    #Liste des biens inscrits
    listeBien = []

    def __init__(self):
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

        #complet deviandra True quand les données seront validées, permet de boucler avant ça
        complet = False


        erreur = False

        while not complet:

            if erreur:
                print("les informations sont incorrectes, veullez réessayer SVP")

                # A FAIRE : vérifier la conformité des infos

            # complet passe à True si les données sont validées
            complet = True
            # erreur passe à True
            erreur = True

        # on incrémente la varible de classe identifiant et on l'affecte à l'identifiant de l'objet
        self.num = BienImmobilier.num
        BienImmobilier.num = BienImmobilier.num + 1

        self.adresse = adresse
        self.orientation = orientation
        self.prixDemande = prixDemande
        self.dateVenteSouhait = dateVenteSouhait
        self.dateDispo = dateDispo
        self.nombrePieces = nombrePieces

        BienImmobilier.listeBien.append(self)

    def afficherTousBiens_adresse(self):
        return BienImmobilier()


"""TESTs"""

b1 = BienImmobilier()
b1.inscrire("loin", "de gauche", "trop", "vite", "maintenant", 1)
print(b1.listeBien)
print(b1.num)

print(b1)
print(BienImmobilier.listeBien[0].orientation + "  res")