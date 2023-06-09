"""
    définition de la classe Utilisateur SQLAlchemy
    (interface vers la table utilisateur)
"""
from domo import db


class Utilisateur(db.Model):
    """Modèle utilisateur pour la base de données"""

    # par défaut, la table aura le nom de la classe en minuscule -> utilisateur
    # pour donner un autre nom de table :
    # __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(80))
    mdp = db.Column(db.String(250))
    email = db.Column(db.String(250), unique=True, nullable=False)
    admin = db.Column(db.Boolean, default=False)

    # exemples de clés étrangères -> on suppose que la table 'classe' existe
    # idClasse = db.Column(db.Integer, db.ForeignKey("classe.id"), nullable=False)

    # ajout de l'attribut d'instance "classe" pour accéder à la classe depuis un utilisateur
    # et d'un attribut "user" pour accéder à la liste des utilisateurs depuis une classe
    # classe = db.relationship("Classe", db.backref("user"))

    def __repr__(self):
        me = f"<User id={self.id} email={self.email},"
        me += f" admin={self.admin}>"
        return me

    # exemples de méthodes de recherche d'un utilisateur
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_public_id(cls, public_id):
        return cls.query.filter_by(public_id=public_id).first()

    def enregistrerMdp(self, mdp):
        self.mdp = mdp
        return True


# Exemples d'utilisation de la classe
"""
Ajout d'un utilisateur
    u = Utilisateur(nom="toto", email="toto@no-log.org")
    u.enregistrerMdp('secret123')
    db.session.add(u)
    db.session.commit()

Sélectionner par la clé
    u = Utilisateur.query.get(24)
-> ex: u.nom renverra alors le nom de l'utilisateur ayant l'id 24

Modifier d'un utilisateur
    dict = {"nom": "toto", "email": "toto@no-log.org", "admin"=False}
    u = Utilisateur.query.get(24)
    for k, v in dict.items():
        setattr(u, k, v)
    db.session.commit()

Sélectionner par filtre WHERE (on pourra aussi utiliser les méthodes in_, and_, or_ etc...)
    u = Utilisateur.query.filter(Utilisateur.nom.like("%" + chaine + "%"))

Jointure
    u = Utilisateur.query.join(Classe)

requête avec champs sélectionnés explicites et sous-requête

    ssReq = db.session.query(Utilisateur.nom, Classe.id)
    .select_from(Utilisateur)
    .join(Classe, Classe.id == Utilisateur.idClasse)
    .filter(Classe.annee == an)
    .subquery()

    req = db.session.query(ssReq.c.nom)
    .select_from(ssReq)
    .distinct()

"""
