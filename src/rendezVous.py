"""Creation de la classe RDV"""

import agence
import TB

class RendezVous:

    #Prend le rendez vous avec le client
    def prendreRDV(self):

        #Inscrit le bien a vendre
        type = "r"

        while (type.lower() != "appart") and (type.lower() != "maison") and (type.lower() != "terrain"):
            type = input("Type de bien, tapez le type de bien a inscrire : appart, maison ou terrain : ")

        return RendezVous.inscriptionBienVendre(self, type)

    # Inscrit un bien
    def inscriptionBienVendre(self, type):

        # Incrémentation de la clé
        agence.Agence.keyB += 1

        if type.lower() == "terrain":
            agence.Agence.listeBien[agence.Agence.keyB] = TB.Terrain.inscrireTerrain(self)
            return agence.Agence.listeBien[agence.Agence.keyB]

        elif type.lower() == "maison":
            agence.Agence.listeBien[agence.Agence.keyB] = TB.Maison.inscrireMaison(self)
            return agence.Agence.listeBien[agence.Agence.keyB]

        elif type.lower() == "appartement":
            agence.Agence.listeBien[agence.Agence.keyB] = TB.Appart.inscrireAppart(self)
            return agence.Agence.listeBien[agence.Agence.keyB]
