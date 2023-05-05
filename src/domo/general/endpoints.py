from flask import (
    Blueprint,
    redirect,
    session,
    url_for,
    render_template,
    request
)

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
    return render_template("auth_connexion.html")

@gen_bp.app_errorhandler(404)
def page_non_trouve(error):
    return render_template("404.html"), 404

dicomdp = {"login@g.com" : "mdp"}
@gen_bp.route("/acceuil", methods=['POST'])
def validermdp():
    entree = request.form
    entreemail = entree['mail']
    entreemdp = entree['mdp']
    for mail in dicomdp:
        if mail == entreemail and dicomdp[mail] == entreemdp:
            return render_template("acceuil.html")
    else : 
        return render_template("auth_connexion.html")
        