from domo.models.donnees_actuelles import Donnees_actuelles
from domo.models.historique import historique

def recuperer_donnees_actuelles():
    """revoie un dictionnaire avec les données actuelles 
       si la valeur n'a pas pu être récuperer mettre _"""
    ventilateur_mode = Donnees_actuelles.query.filter_by(type_de_donnees='ventilateur_mode').first()
    ventilateur_ctrl = Donnees_actuelles.query.filter_by(type_de_donnees='ventilateur_ctrl').first()
    ventilateur_set_temp_seuil = Donnees_actuelles.query.filter_by(type_de_donnees='ventilateur_set_temp_seuil').first()
    latest_temp = historique.query.order_by(desc(historique.date_et_heur_prise)).limit(1).all()
    dico["temp"] = latest_temp.temperature
    dico["humidité"] = latest_temp.humidite
    dico["ventilateur_mode"] = ventilateur_mode.valeur
    dico["ventilateur_ctrl"] = ventilateur_ctrl.valeur
    dico["ventilateur_set_temp_seuil"] = ventilateur_set_temp_seuil.valeur
    dico = {}
    return dico

def activer_ventilateur(on_off) -> None:
    """Publie la modification via MQTT : 
        -> mode 0 (manuel) et ctrl en fonction de la variable on_off   
       la modif sera ensuite enregistrée en base de données"""
    pass

def mode_auto_ventilateur(set_temp_seuil) -> None:
    """Publie la modification via MQTT : 
        -> mode 1 (auto) et set_temp_seuil avec la température en paramètre
       la modif sera ensuite enregistrée en base de données"""
    pass

dicorgb = {"rouge" : [255, 0, 0], "vert" : [0, 255, 0], "bleu" : [0, 0, 255]}
def couleurstoRGB(couleurs):
    """fonction qui convertit la couleur en RGB, un tableau d'entiers"""
    for key in dicorgb:
        if key == couleurs:
            return dicorgb[key]


def gerer_lumieres(couleurs) -> None:
    """Publie la modification via MQTT : 
        -> les 3 composantes sont envoyées sur les 3 topics définis sur le drive (12 mai)
       la modif sera ensuite enregistrée en base de données"""
    rgb = couleurstoRGB(couleurs)
    return rgb