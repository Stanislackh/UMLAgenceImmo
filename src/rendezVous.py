"""Creation de la classe RDV"""

import agence
import TB
import promesseVente

class RendezVous:

    #Prend le rendez vous avec le client
    def prendreRDV(self):

        #Inscrit le bien a vendre
        type = "r"

        while (type.lower() != "appartement") and (type.lower() != "maison") and (type.lower() != "terrain"):
            type = input("Type de bien, tapez le type de bien a inscrire : appartement, maison ou terrain : ")

        return RendezVous.inscriptionBienVendre(self, type)

    # Inscrit un bien
    def inscriptionBienVendre(self, type):

        # Incrémentation de la clé
        agence.Agence.keyB += 1

        if type.lower() == "terrain":
            agence.Agence.listeBien[agence.Agence.keyB] = type, TB.Terrain.inscrireTerrain(self)
            return agence.Agence.listeBien[agence.Agence.keyB]

        elif type.lower() == "maison":
            agence.Agence.listeBien[agence.Agence.keyB] = type, TB.Maison.inscrireMaison(self)
            return agence.Agence.listeBien[agence.Agence.keyB]

        elif type.lower() == "appartement":
            agence.Agence.listeBien[agence.Agence.keyB] = type, TB.Appart.inscrireAppart(self)
            return agence.Agence.listeBien[agence.Agence.keyB]


    def confirmerVente(self, rep="r"):

        print("Rendez-Vous pris !")

        while (rep.lower() != "oui") and (rep.lower() != "non"):
            rep = input("Voulez vous acheter ce bien ? : ")

        if rep == "oui":
            #signature de la promesse de vente
            promesseVente.PromesseVente.signature(self)

        if rep == "non":
            print("a plus tard")