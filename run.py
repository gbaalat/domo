"""
    Flask CLI : accès depuis la ligne de commande
    
    Les modèles SQLAlchemy (comme Utilisateur) doivent être importés
    dans ce fichier pour être détectés par Flask-Migrate
"""
import os

from domo import create_app, db
from domo.models.utilisateur import Utilisateur
from domo.models.donnees_actuelles import Donnees_actuelles
from domo.models.etat_lumiere import etat_lumiere
from domo.models.historique import historique

app = create_app(os.getenv("FLASK_ENV", "development"))

@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Utilisateur": Utilisateur,
        "Donnees_actuelles": Donnees_actuelles,
        "etat_lumiere": etat_lumiere,
        "historique": historique
    }

