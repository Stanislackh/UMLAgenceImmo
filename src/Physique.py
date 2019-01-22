"""Classe Physique
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
from Personnes import Personnes

class Physique(Personnes):

    def __init__(self, pfnom = "", pfprenom = "", pfadresse = "",pftelephone = 0, pfmail = ""):
        Personnes.__init__( self,pfnom = "", pfprenom = "", pfadresse = "",pftelephone = 0, pfmail = "")
