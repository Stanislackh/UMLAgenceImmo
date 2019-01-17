"""Classe Personnes
Attributs :
- Id
- Nom
- Prenom
- Adresse
- Telephone
- Mail
Methodes :
- ajoutClient()
- afficherInfosClient()
-
-
-
"""
import re

class Personnes:

    # Initialise l'incrémentation des personnes
    identifiant = 0

    # Initialisation de la liste de clients
    clients = {}

    # Initialisation de la classe avec les 5 Attibuts
    def __init__(self, pfnom = "", pfadresse = "",pftelephone = 0, pfmail = ""):

      self.nom = pfnom
      self.adresse = pfadresse
      self.telephone = pftelephone
      self.mail = pfmail

    #Permet d'ajouter un nouveau client
    def ajouterClientPhysique(self):
        #Elements de l'adresse
        res = []
        numero = 0
        chemin = ""
        cp = 0
        ville = ""

        #Entrée des données par l'utilisateur
        self.nom = input("Entrez le nom du nouveau client : ")

        numero = int(input("Entrez le numéro d'adresse : "))
        chemin = input("Entrez le nom de la rue : ")
        cp = int(input("Entrez le code postal : "))
        ville = input("Entrez la ville : ")

        res.append(numero)
        res.append(chemin)
        res.append(cp)
        res.append(ville)

        self.adresse = res
        self.telephone = str(input("Entrez le téléphone du nouveau client : "))
        self.mail = input("Entrez le mail du nouveau client : ")

        #Incrémentation du nombre de clients de 1
        Personnes.identifiant = Personnes.identifiant + 1

        #Ajoute les élements dans le dictionnaire
        self.clients[self.identifiant] = Personnes(self.nom,self.adresse,self.telephone,self.mail)

    #Permet d'afficher les infos pour le client selectionné
    def afficherInfosClient(self, IdPersonne):
        print(Personnes.clients[IdPersonne])

    #Permet d'afficher les informations de l'objet
    def __str__(self):
      return "Infos du client => Id Client : {}; Nom : {}; Téléphone : {}; Adresse : {}; Mail : {}".format(self.identifiant, self.nom, self.prenom, self.telephone, self.adresse, self.mail)


"""Données de tests

p = Personnes()
p.ajouterClientPhysique()
print("p :", p)"""

