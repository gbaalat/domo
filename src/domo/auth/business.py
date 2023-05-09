"""
Ici, on trouve les fonctions principales pour la gestion de l'authentification
"""
from domo.models.utilisateur import Utilisateur
from domo import db

dicomdp = {"login@g.com" : "mdp"}
def test_utilisateur(email):
    """fonction factice"""
    return Utilisateur.find_by_email(email)

def valider_connexion(entreemail, entreemdp):
    for mail in dicomdp:
        return mail == entreemail and dicomdp[mail] == entreemdp