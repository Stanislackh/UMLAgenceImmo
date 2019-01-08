"""Classe Personnes
Attributs :
- Id
- Nom
- Prenom
- Adresse
- Telephone
- Mail
Methodes :
- AjoutClient()
-
-
-
-
"""


class Personne:
    # Initialise l'incrémentation des personnes
    identifiant = 0
    # Initialisation de la liste de clients
    clients = {}

    # Initialisation de la classe avec les 5 Attibuts
    def __init__(self, pfnom, pfprenom, pftelephone, pfmail):
        self.nom = pfnom
        self.prenom = pfprenom
        self.telephone = pftelephone
        self.mail = pfmail
        Personne.identifiant = 1 + Personne.identifiant

    def AjoutDico(self):
        self.clients[self.identifiant] = self.nom + " " + self.prenom + " " + self.telephone + " " + self.mail


"""TESTS"""

p1 = Personne("joe", "trede", "0241512131", "joe@trede")
# print(p1.nom)
p1.AjoutDico()
# print(p1.clients)

p2 = Personne("joyooode", "trede", "0241512131", "joe@trede")
p2.AjoutDico()

print(Personne.clients)