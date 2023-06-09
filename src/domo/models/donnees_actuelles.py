from domo import db
from datetime import datetime

class Donnees_actuelles(db.Model):
    """Modèle donnees actuelles pour la base de données"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_de_donnees = db.Column(db.String(50))
    """ type de donnees:
        ventilateur_mode
        ventilateur_ctrl
        ventilateur_actifs
    """
    date_et_heur_prise = db.Column(db.DateTime, default=datetime.now())
    valeur = db.Column(db.Integer)


    def __repr__(self):
        me = f"<valeur={self.valeur},"
        me += f" date_et_heur_prise={self.date_et_heur_prise}, type_de_donnees={self.type_de_donnees}>"
        return me
    
