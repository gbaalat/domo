def recuperer_donnees_actuelles():
    """revoie un dictionnaire avec les données actuelles si la valeur n'a pas pu être récuperer mettre _"""
    dico = {'temp' : 20, 'ventilateur' : "manuel", 'humidité' : 87}
    return dico

def activer_ventilateur_auto(on_off):
    """Modifie la base de données avec ventilateur allumé (ON) ou éteint (OFF), ne renvoie rien"""
    pass

def activer_ventilateur_manu(temp):
    pass

dicorgb = {"rouge" : [255, 0, 0], "vert" : [0, 255, 0], "bleu" : [0, 0, 255]}
def couleurstoRGB(couleurs):
    """fonction qui convertit la couleur en RGB, un tableau d'entiers"""
    for key in dicorgb:
        if key == couleurs:
            return dicorgb[key]


def gerer_lumieres(couleurs):
    """Modifie la base de données et change la couleur de la lumière, ne renvoie rien"""
    rgb = couleurstoRGB(couleurs)
    pass
