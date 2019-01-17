from Personnes import Personnes

class Morale(Personnes):


    #Initialise une personne morale avec le numero de SIREN et le forme juridique de l'entreprise
    def __init__(self, pfnoSiren= "", pfformeJuridique = "", pfnom = "", pfadresse = "", pftelephone = 0, pfmail = ""):
        Personnes.__init__(self, pfnom = "", pfadresse = "", pftelephone = 0, pfmail = "")
        self.noSiren = pfnoSiren
        self.formeJuridique = pfformeJuridique


    def ajouterPersonneMorale(self):
        Personnes.ajouterClientPhysique(self)
        self.formeJuridique = input("Entrez la forme juridique : ")
        self.noSiren = input("Entrez le numéro de SIREN : ")

        # Incrémentation du nombre de clients de 1
        Personnes.identifiant = Personnes.identifiant + 1

        # Ajoute les élements dans le dictionnaire
        self.clients[self.identifiant] = Morale(self.noSiren, self.formeJuridique, self.nom,self.adresse, self.telephone, self.mail)

    def __str__(self):
        return "Infos du client => Id Client : {}; Numéro SIREN : {}; Forme juridique : {};" \
               "  Nom : {}; Téléphone : {}; Adresse : {}; Mail : {}"\
            .format(self.identifiant, self.noSiren, self.formeJuridique, self.nom,
                    self.telephone, self.adresse, self.mail)


    """Données de Tests"""

m = Morale()
m.ajouterPersonneMorale()
print(m)

