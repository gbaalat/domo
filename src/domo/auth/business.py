"""
Ici, on trouve les fonctions principales pour la gestion de l'authentification
"""
from domo.models.utilisateur import Utilisateur
from domo import db


def test_utilisateur(email):
    """test si un email exist deja dans la base de donners si oui revois False sinon renvois True"""
    u= Utilisateur.query.filter(Utilisateur.email==email).first()
    if u is None:
        return True
    else:
        return False

dicomdp = {"login@g.com" : "mdp"}
def valider_connexion(entreemail, entreemdp):
    """renvoie un booléen indiquant si les identifiants sont valides"""
    u = Utilisateur.query.filter(Utilisateur.email==entreemail).first()
    if u is not None:
        if u.mdp == entreemdp:     
            return True
    return False

def enregistre_utilisateur(email,mdp):
    """enregistre un utiisateur dans a base de donner"""
    u = Utilisateur(email=email)
    u.enregistrerMdp(mdp)
    db.session.add(u)
    db.session.commit()