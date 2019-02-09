import re

class BI:
    "classe definissant les biens immobiliers"

    def __init__(self, pfnum = 0, pfadresse ="3 rue picard 11111 cypres" , pfprixDemande = 0, pfdateVenteSouhait = "01/01/2018", pfdateDispo = "01/01/2018"):
        self.adresse = pfadresse
        self.prixDemande = pfprixDemande
        self.dateVenteSouhait = pfdateVenteSouhait
        self.dateDispo = pfdateDispo

    #Ajoute un bien selon le type
    def ajouterBien(self, pfnum = 0, pfadresse ="3 rue picard 11111 cypres" , pfprixDemande = 0, pfdateVenteSouhait = "01/01/2018", pfdateDispo = "01/01/2018"):
        self.adresse = input("adresse : ")
        self.prixDemande = input("prix demandé : ")
        self.dateVenteSouhait = input("date de vente souhaité : ")
        self.dateDispo = input("date de disponibilité : ")



    def afficherTousBiens_adresse(self):
        for i in BI.listeBien.keys():
            yield BI.listeBien[i].adresse

    def __str__(self):
        return "bien immobilier n°" + str(self.num) + " adresse: " + self.adresse

    def __repr__(self):
        return "" + self.adresse


"""TESTs"""
if __name__ == "__main__":
    print(0)
    # a = BI()
    # a.appendListe(200, "3 rue picard 11111 cypres", "200000", "02/01/2018", "01/01/2019")
    # print("je suis la liste incrémentée : " + str(BI.listeBien))

    #
    # b1 = BI()
    # b1.inscription("terrain")
    #
    # #b1.appendListe(200, "3 rue picard 11111 cypres", "200000", "02/01/2018", "01/01/2019")
    # print(str(BI.listeBien) + "  ,  listeBien après inscription de b1")
    # print(str(TB.Terrain.listeBien) + "  ,  listeBien de Terrain")
    # print(str(b1.num) + ", num de b1")

    # b2 = BI()
    # #b2.inscription(15, 3, 150, "3 rue picard 11111 cypres", "200000", "02/01/2018", "01/01/2019")
    # b2.inscription("maison")
    #
    # print(str(BI.listeBien) + "  ,  listeBien après inscription de b2")
    # print(str(TB.Maison.listeBien) + " , liste appart")
    # print(str(b2.num) + ", num de b2")
    #
    # b3 = BI()
    # # b2.inscription(15, 3, 150, "3 rue picard 11111 cypres", "200000", "02/01/2018", "01/01/2019")
    # b3.inscription("appartement")
    #
    # print(str(BI.listeBien) + "  ,  listeBien après inscription de b3")
    # print(str(TB.Maison.listeBien) + " , liste appart")
    # print(str(b3.num) + ", num de b3")

    # for i in afficherTousBiens_adresse():
    #     print(str(i) + "    afficher tous les biens")
    #
    # print(BienImmobilier.listeBien.keys())

