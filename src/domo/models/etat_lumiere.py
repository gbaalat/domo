from domo import db

class Etat_lumiere(db.Model):
    """Modèle donnees actuelles pour la base de données"""
    
    id_lumiere = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rouge = db.Column(db.Integer)
    vert = db.Column(db.Integer)
    bleu = db.Column(db.Integer)


    def __repr__(self):
        me = f"<donnees id_lumiere={self.id_lumiere}"
        me += f" bleu={self.bleu}, verts={self.vert}, rouge={self.rouge}>"
        return me