from domo.models.donnees_actuelles import Donnees_actuelles 
from domo.models.historique import Historique 
from domo.mqtt.publication import publish
from domo.util.decorators import admin

def recuperer_donnees_actuelles():
    """revoie un dictionnaire avec les données actuelles 
       si la valeur n'a pas pu être récuperer mettre _"""
    dico ={}
    mode = Donnees_actuelles.query.filter(Donnees_actuelles.type_de_donnees=='ventilateur_mode').first()
    ctrl = Donnees_actuelles.query.filter(Donnees_actuelles.type_de_donnees=='ventilateur_ctrl').first()
    actif = Donnees_actuelles.query.filter(Donnees_actuelles.type_de_donnees=='ventilateur_actifs').first()
    temp = Historique.query.order_by(Historique.date_et_heur_prise.desc()).first()
    hum = Historique.query.order_by(Historique.date_et_heur_prise.desc()).first()
    # "or" pour gérer des valeurs par défaut : si pas de données (None) .valeur plante
    dico["ventilateur_mode"] = 1 if mode is None else mode.valeur
    dico["ventilateur_ctrl"] = 0 if ctrl is None else ctrl.valeur
    dico["ventilateur"] = 0 if actif is None else actif.valeur
    dico["temp"] = -274 if temp is None else temp.temperature
    dico["humidité"] = -1 if hum is None else hum.humidite
    return dico

@admin
def activer_ventilateur_manu(on_off) -> None:
    """Publie la modification via MQTT : 
        -> mode 0 (manuel) et ctrl en fonction de la variable on_off   
       la modif sera ensuite enregistrée en base de données"""
    publish("Maison/Ventilateur/Mode/", "0")
    publish("Maison/Ventilateur/Ctrl/", str(on_off))

@admin
def mode_auto_ventilateur(set_temp_seuil) -> None:
    """Publie la modification via MQTT : 
        -> mode 1 (auto) et set_temp_seuil avec la température en paramètre
       la modif sera ensuite enregistrée en base de données"""
    publish("Maison/Ventilateur/Mode/", "1")
    publish("Maison/Ventilateur/Set_temp_seuil/", str(set_temp_seuil))

dicorgb = {"rouge" : [255, 0, 0], "vert" : [0, 255, 0], "bleu" : [0, 0, 255]}
def couleurstoRGB(couleurs):
    """fonction qui convertit la couleur en RGB, un tableau d'entiers"""
    for key in dicorgb:
        if key == couleurs:
            return dicorgb[key]

@admin
def gerer_lumieres(couleurs) -> None:
    """Publie la modification via MQTT : 
        -> les 3 composantes sont envoyées sur les 3 topics définis sur le drive (12 mai)
       la modif sera ensuite enregistrée en base de données"""
    rgb = couleurstoRGB(couleurs)
    return rgb
