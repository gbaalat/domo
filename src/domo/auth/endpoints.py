from flask import Blueprint, redirect, render_template, request, flash, url_for, session
from domo.auth.business import test_utilisateur

auth_bp = Blueprint(
    "auth_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/auth",
)

@auth_bp.route("/inscription", methods=["GET", "POST"])
def inscription():
    """Exemple fictif de gestion de l'inscription:
       on suppose que id est rentrée dans l'objet session de Flask
       lorsque l'utilisateur est connecté"""
    if "id" in session:
        return redirect(url_for("gen_bp.home")),flash("Déconnectez-vous pour vous inscrire.")
    if request.method == "POST":
        email=str(request.form["email"]) #recup du champ mail du formulaire HTML
        if test_utilisateur(email): #fonction dans business.py
            session['id'] = email #identificateur de connexion
            flash(f"email OK") #message à destination de l'utilisateur
        else:
            flash("email incorrect")
    return render_template("auth_inscription.html")


@auth_bp.route("/connexion", methods=["GET", "POST"])
def connexion():
    if "id" in session: #déjà connecté
        flash("Déconnectez-vous pour vous connecter à un autre compte.")
        redirect(url_for("gen_bp.home"))
    if request.method == "POST":
        #gestion du formulaire saisi par l'utilisateur
        pass
    return render_template("auth_connexion.html")


@auth_bp.route("/deconnexion")
def deconnexion():
    session.pop("id") # on supprime id de l'objet session
    flash("Vous vous êtes bien déconnecté(e)")
    return redirect(url_for("gen_bp.home"))