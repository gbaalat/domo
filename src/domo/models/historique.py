from domo import db
from datetime import datetime

class historique(db.Model):
    """Modèle temperature actuelle pour la base de données"""
    date_et_heur_prise = db.Column(db.DateTime, default=datetime.now())
    temperature = db.Column(db.Integer)
    humidite = db.Column(db.Integer)
    id_historique = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        me = f"<historique id_temperature={self.id_historique} temperature={self.temperature},humidite={self.humidite},"
        me += f" date_et_heur_prise={self.date_et_heur_prise}>"
        return me