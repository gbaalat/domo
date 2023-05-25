from domo import db

class etat_lumiere(db.Model):
    """Modèle donnees actuelles pour la base de données"""
    rouge = db.column(db.Interger)
    verts = db.column(db.Interger)
    bleu = db.column(db.Interger)
    id_lumiere = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        me = f"<donnees id_lumiere={self.id_lumiere}"
        me += f" bleu={self.date_et_heur_prbleuise}, verts={self.verts}, rouge={self.rouge}>"
        return me