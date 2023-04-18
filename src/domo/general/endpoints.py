from flask import (
    Blueprint,
    redirect,
    session,
    url_for,
    render_template,
)

gen_bp = Blueprint(
    "gen_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/gen",
)

@gen_bp.route("/")
def home():
    """renvoie vers l'écran d'accueil"""
    return render_template("acceuil.html")

@gen_bp.app_errorhandler(404)
def page_non_trouve(error):
    return render_template("404.html"), 404
