"""Classe Personnes"""

import re

class Personnes:
    # Initialisation de la classe avec les 5 Attibuts
    def __init__(self, pfnom = "", pfadresse = "",pftelephone = 0, pfmail = ""):

      self.nom = pfnom
      self.adresse = pfadresse
      self.telephone = pftelephone
      self.mail = pfmail

    #Permet d'ajouter un nouveau client
    def ajouterClient(self):

        #Elements de l'adresse
        res = []
        numero = 0
        chemin = ""
        cp = 0
        ville = ""

        #Entrée des données par l'utilisateur
        self.nom = input("Entrez le nom du nouveau client : ")
        self.telephone = str(input("Entrez le téléphone du nouveau client : "))

        numero = input("Entrez le numéro d'adresse : ")
        chemin = input("Entrez le nom de la rue : ")
        cp = input("Entrez le code postal : ")
        ville = input("Entrez la ville : ")

        res.append(numero)
        res.append(chemin)
        res.append(cp)
        res.append(ville)

        self.adresse = res
        self.mail = input("Entrez le mail du nouveau client : ")

        return self.nom, self.telephone, self.adresse, self.mail

    #Permet d'afficher les informations de l'objet
    def __str__(self):
      return "Infos du client => Nom : {}; Téléphone : {}; Adresse : {}; Mail : {}".format(
          self.nom, self.telephone, self.adresse, self.mail)
