"""Classe Morale
Attributs :
-
-
-
-
Methodes :
-
-
-
-
-
"""
import Personnes

class Morale(Personnes):

    #Initialise une personne morale avec le numero de SIREN et le forme juridique de l'entreprise
    def __init__(self, pfnoSiren, pfformeJuridique, pfnom = "", pfprenom = "", pfadresse = "", pftelephone = 0, pfmail = ""):
        Personnes.Personnes.__init__(self, pfnom = "", pfprenom = "", pfadresse = "", pftelephone = 0, pfmail = "")
        self.noSiren = pfnoSiren
        self.formeJuridique = pfformeJuridique


    def ajouterPersonneMorale(self):
        self.formeJuridique = input("Entrez la forme juridique : ")
        self.noSiren = input("Entrez le numéro de SIREN : ")

        # Incrémentation du nombre de clients de 1
        Personnes.Personnes.identifiant = Personnes.Personnes.identifiant + 1

        # Ajoute les élements dans le dictionnaire
        self.clients[self.identifiant] = Morale(self.noSiren, self.formeJuridique, self.nom, self.prenom,self.adresse, self.telephone, self.mail)

    def __str__(self):
        return "Infos du client => Id Client : {}; Numéro SIREN : {}; Forme juridique : {};" \
               "  Nom : {}; Prenom : {}; Téléphone : {}; Adresse : {}; Mail : {}"\
            .format(self.identifiant, self.noSiren, self.formeJuridique, self.nom, self.prenom,
                    self.telephone, self.adresse, self.mail)
