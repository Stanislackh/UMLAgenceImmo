"""Creation de la classe RDV"""

from Personnes import Personnes
from Mandat import Mandat

class RDV:

    def __init__(self):
        self.adresse = ""

    #Prend le rendez vous avec le client
    def PrendreRDV(self):
        #Ajoute un client qui désire vendre
        Personnes.ajouterClientPhysique()

        #Crée un mendat de vente
        Mandat.vente()



