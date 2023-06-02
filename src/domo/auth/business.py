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
    """renvoie un booléen indiquant si les identifiants sont valides"""
    u = Utilisateur.query.filter(Utilisateur.email==entreemail).first()
    if u is not None:
        if u.mdp == entreemdp:     
            return True
    return False