"""Creation de la classe RDV"""

class RDV:

    #Prend le rendez vous avec le client
    def PrendreRDV(self):

        #Inscrit le bien a vendre
        type = "r"

        while (type.lower() != "appart") and (type.lower() != "maison") and (type.lower() != "terrain"):
            type = input("Type de bien, tapez le type de bien a inscrire : appart, maison ou terrain : ")

        #renvoi un bien a vendre avec le mendat de vente
        return Mendat.autorisation(self), Agence.inscriptionBienVendre(self,type)




