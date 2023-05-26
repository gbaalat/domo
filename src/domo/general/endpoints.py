from flask import (
    Blueprint,
    redirect,
    session,
    url_for,
    render_template,
    request,
    jsonify
)
from domo.general.business import recuperer_donnees_actuelles, activer_ventilateur_auto, activer_ventilateur_manu, gerer_lumieres

gen_bp = Blueprint(
    "gen_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="",
)

@gen_bp.route("/")
def home():
    """renvoie vers l'écran d'accueil"""
    if "mail" in session:
        return redirect(url_for("gen_bp.acceuil"))
    else :
        return redirect(url_for("auth_bp.connexion"))


@gen_bp.route("/commandes")
def commandes():
    if "mail" in session:
        return render_template("commandes_manu.html")
    else : 
        return redirect(url_for("gen_bp.home"))

@gen_bp.route("/acceuil")
def acceuil():
    if "mail" in session:
        return render_template("acceuil.html", session=session, dico=recuperer_donnees_actuelles())
    else : 
        return redirect(url_for("gen_bp.home"))

@gen_bp.app_errorhandler(404)
def page_non_trouve(error):
    return render_template("404.html"), 404
        
@gen_bp.route("/activventilateur/manu", methods=['POST'])
def manu_ventilo():
    if "mail" in session:
        on_off = request.json["value"]  # axios envoie les données en json -> request.json au lieu de request.form
        activer_ventilateur_auto(on_off)
        return jsonify({"ven": True}) # renvoie un "accusé réception" au format json
    return jsonify({"ven": False})    # ici, pas connecté !

@gen_bp.route("/activventilateur/auto", methods=['POST'])
def auto_ventilo():
    if"mail" in session: 
        temp = int(request.json["temp"])
        activer_ventilateur_manu(temp)
        return jsonify({"ven": temp})
    return jsonify({"ven": False})

    
@gen_bp.route("/lumieres", methods=['POST'])
def lumieres():
    if 'mail' in session:
        lum = request.json["value"]  # axios envoie les données en json -> request.json au lieu de request.form
        gerer_lumieres(lum)
        return jsonify({"lum": True}) # renvoie un "accusé réception" au format json
    return jsonify({"lum": False})    # ici, pas connecté !

