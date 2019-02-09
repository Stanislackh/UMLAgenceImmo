import TB
import re

class BI:
    "classe definissant les biens immobiliers"

    # identifiant unique incrémenté à chaque instanciation
    num = 1

    # Liste des biens inscrits
    listeBien = {}

    def __init__(self, pfnum = 0, pfadresse ="3 rue picard 11111 cypres" , pfprixDemande = 0, pfdateVenteSouhait = "01/01/2018", pfdateDispo = "01/01/2018"):
        "Un bien a un identifiant unique, une adresse, une orientation, un prix demandé, un date de vente souhaitée, une disponibilité, et un nombre de pièces = 0 si il s'agit d'un terrain"
        self.num = pfnum
        self.adresse = pfadresse
        self.prixDemande = pfprixDemande
        self.dateVenteSouhait = pfdateVenteSouhait
        self.dateDispo = pfdateDispo

    def __str__(self):
        return "bien immobilier n°" + str(self.num) + " adresse: " + self.adresse

    def __repr__(self):
        return "" + self.adresse

    def inscrire(self, adresse, prixDemande, dateVenteSouhait, dateDispo):
        """permet de créer un bien, de vérifier les paramètres et de l'enregistrer dans les biens inscrit dans l'agence ; adresse ; prix demandé ; date de vente souhaité ; date de disponnibilité"""

# erreur permet de savoir si l'inscription sera validée. Si erreur = True, le bien ne sera pas inscrit
        erreur = False

# vérification de l'adresse entrée
        exp_reg_adresse = re.compile(r"^([0-9]{0,4}\s(bis\s){0,1}(rue){0,1}(boulevard){0,1}(avenue){0,1}\s[a-z\s]+[0-9]{5}\s[a-z]+)$")
        essai_adresse = adresse.lower()
        result_adresse = re.match(exp_reg_adresse, essai_adresse)

        if result_adresse is None:
            print(essai_adresse, "n’est pas une adresse valide")
            erreur = True

        #if

# vérification du prix demandé
        try:
            essai_prixDemande = int(prixDemande)
        except:
            print(prixDemande, "n’est pas un prix valide")

# vérification de la date de vente souhaité
        exp_reg_dateVenteSouhait = re.compile(r"^([0-3][0-9]/[0-1][0-9]/20[1-2][0-9])$")
        essai_dateVenteSouhait = dateVenteSouhait
        result_dateVenteSouhait = re.match(exp_reg_dateVenteSouhait, essai_dateVenteSouhait)

        if result_dateVenteSouhait is None:
            print(essai_dateVenteSouhait, " n’est pas une date valide")
            erreur = True

# vérification de la date de disponibilité
        exp_reg_dateDispo = re.compile(r"^([0-3][0-9]/[0-1][0-9]/20[1-2][0-9])$")
        essai_dateDispo = dateDispo
        result_dateDispo = re.match(exp_reg_dateDispo, essai_dateDispo)

        if result_dateDispo is None:
            print(essai_dateDispo, " n’est pas une date valide")
            erreur = True

        # on vérifie que les données soient valides avant d'inscrire
        if not erreur:

            # on incrémente la varible de classe identifiant et on l'affecte à l'identifiant de l'objet
            self.num = BI.num
            BI.num = BI.num + 1

            # On affecte
            self.adresse = adresse
            self.prixDemande = essai_prixDemande
            self.dateVenteSouhait = dateVenteSouhait
            self.dateDispo = dateDispo

        else:
            print("il y a eu une erreur")

    def inscription(self, type):

        if type.lower() == "terrain":
            BI.listeBien[BI.num] = TB.Terrain.inscrireTerrain(self)
            print("Dico bon : " + str(BI.listeBien))
            BI.num += 1

        elif type.lower() == "maison":
            BI.listeBien[BI.num] = TB.Maison.inscrireMaison(self)
            print("Dico bon : " + str(BI.listeBien))
            BI.num += 1

        elif type.lower() == "appartement":
            BI.listeBien[BI.num] = TB.Appart.inscrireAppart(self)
            print("Dico bon : " + str(BI.listeBien))
            BI.num += 1


    def afficherTousBiens_adresse(self):
        for i in BI.listeBien.keys():
            yield BI.listeBien[i].adresse

    def appendListe(self, adresse, prixDemande, dateVenteSouhait, dateDispo):
        BI.listeBien[BI.num] = TB.TB.inscrireTerrain(self)
        BI.num += 1


"""TESTs"""
if __name__ == "__main__":

    # a = BI()
    # a.appendListe(200, "3 rue picard 11111 cypres", "200000", "02/01/2018", "01/01/2019")
    # print("je suis la liste incrémentée : " + str(BI.listeBien))


    b1 = BI()
    b1.inscription("terrain")

    #b1.appendListe(200, "3 rue picard 11111 cypres", "200000", "02/01/2018", "01/01/2019")
    print(str(BI.listeBien) + "  ,  listeBien après inscription de b1")
    print(str(TB.Terrain.listeBien) + "  ,  listeBien de Terrain")
    print(str(b1.num) + ", num de b1")

    b2 = BI()
    #b2.inscription(15, 3, 150, "3 rue picard 11111 cypres", "200000", "02/01/2018", "01/01/2019")
    b2.inscription("maison")

    print(str(BI.listeBien) + "  ,  listeBien après inscription de b2")
    print(str(TB.Maison.listeBien) + " , liste appart")
    print(str(b2.num) + ", num de b2")

    b3 = BI()
    # b2.inscription(15, 3, 150, "3 rue picard 11111 cypres", "200000", "02/01/2018", "01/01/2019")
    b3.inscription("appartement")

    print(str(BI.listeBien) + "  ,  listeBien après inscription de b3")
    print(str(TB.Maison.listeBien) + " , liste appart")
    print(str(b3.num) + ", num de b3")

    # for i in afficherTousBiens_adresse():
    #     print(str(i) + "    afficher tous les biens")
    #
    # print(BienImmobilier.listeBien.keys())

