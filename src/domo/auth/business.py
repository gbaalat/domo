"""
Ici, on trouve les fonctions principales pour la gestion de l'authentification
"""
from domo.models.utilisateur import Utilisateur
from domo import db


def test_utilisateur(email):
    """fonction factice"""
    return True # Utilisateur.find_by_email(email)

dicomdp = {"login@g.com" : "mdp"}
def valider_connexion(entreemail, entreemdp):
    for key in dicomdp:
        if key == entreemail and dicomdp[key] == entreemdp:
            return True
    return False