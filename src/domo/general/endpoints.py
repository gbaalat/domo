from flask import (
    Blueprint,
    redirect,
    session,
    url_for,
    render_template,
    request
)
from domo.general.business import recuperer_donnees_actuelles

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
    return render_template("commandes_manu.html")

@gen_bp.route("/acceuil")
def acceuil():
    return render_template("acceuil.html", session=session, dico=recuperer_donnees_actuelles())

@gen_bp.app_errorhandler(404)
def page_non_trouve(error):
    return render_template("404.html"), 404


        