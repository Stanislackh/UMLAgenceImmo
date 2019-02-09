from personnes import Personnes

class Morale(Personnes):


    #Initialise une personne morale avec le numero de SIREN et le forme juridique de l'entreprise
    def __init__(self, pfnoSiren= "", pfformeJuridique = "", pfnom = "", pfadresse = "", pftelephone = 0, pfmail = ""):
        Personnes.__init__(self, pfnom = "", pfadresse = "", pftelephone = 0, pfmail = "")
        self.noSiren = pfnoSiren
        self.formeJuridique = pfformeJuridique


    def ajouterPersonneMorale(self):
        Personnes.ajouterClient(self)
        self.formeJuridique = input("Entrez la forme juridique : ")
        self.noSiren = int(input("Entrez le numéro de SIREN : "))

        return self.nom, self.telephone, self.adresse, self.mail, self.formeJuridique, self.noSiren
