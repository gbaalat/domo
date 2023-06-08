from domo.models.utilisateur import Utilisateur
from flask import session

def admin(func):
    def wrapper(*arg):
        mail = session["mail"]
        user = Utilisateur.query.filter(Utilisateur.email==mail).first()
        if user is not None and user.admin : 
            func(*arg)
    return wrapper
        
        

        
