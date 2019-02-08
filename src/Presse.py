"""Creation de la classe Presse"""

class Presse:

    presse = {}
    key = 0

    def __init__(self):
        pass

    #Ajoute un article de presse
    def ajouterPresse(self, pftitre, pfbien):

        #Incrémente la clé
        Presse.key += 1

        #Ajoute l'article de presse
        Presse.presse[Presse.key] = (pftitre, pfbien)
        print(Presse.presse)

    #supprime un article existant
    def supprimerPresse(self, pftitre):
        print(Presse.presse.get(self))
        for i in Presse.presse.values():
            key = Presse.presse.keys()
            print(key)
            if pftitre == i[0]:
                if Presse.presse.get(key):
                    Presse.presse.pop(key)
            else:
                print("failed")





"""Tests"""

a = Presse()
print(a.ajouterPresse("joe", "joe"))
a.supprimerPresse("joe")