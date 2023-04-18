"""
Ici, on trouve les fonctions principales pour la gestion de l'authentification
"""
from domo.models.utilisateur import Utilisateur
from domo import db


def test_utilisateur(email):
    """fonction factice"""
    return Utilisateur.find_by_email(email)
