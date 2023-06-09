from domo import db
from datetime import datetime

class Historique(db.Model):
    """Modèle temperature actuelle pour la base de données"""
    date_et_heur_prise = db.Column(db.DateTime, default=datetime.now())
    type_de_donnees = db.Column(db.String(15))
    """ type de donnees:
            temperature
            humidite
    """
    valeur = db.Column(db.Integer)
    id_historique = db.Column(db.Integer, primary_key=True, autoincrement=True)


    def __repr__(self):
        me = f"<historique id_temperature={self.id_historique} valeur={self.valeur},type_de_donnees={self.type_de_donnees},"
        me += f" date_et_heur_prise={self.date_et_heur_prise}>"
        return me