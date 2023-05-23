def recuperer_donnees_actuelles():
    """revoie un dictionnaire avec les données actuelles 
       si la valeur n'a pas pu être récuperer mettre _"""
    dico = {'temp' : 20, 'ventilateur' : None, 'humidité' : 87}
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
