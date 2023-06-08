from flask import Blueprint, redirect, render_template, request, flash, url_for, session
from domo.auth.business import test_utilisateur, valider_connexion, enregistre_utilisateur

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
    if "mail" in session:
        return redirect(url_for("gen_bp.home")),flash("Log out to register")
    if request.method == "POST":
        email=str(request.form["mail"]) #recup du champ mail du formulaire HTML
        if test_utilisateur(email): #test si le emai existe deja
            session['mail'] = email #identificateur de connexion
            mdp=str(request.form["mdp"]) #recup du champ mdp du formulaire HTML
            enregistre_utilisateur(email,mdp)
            flash(f"valid email") #message à destination de l'utilisateur
        else:
            flash("email already exists")
    return render_template("auth_inscription.html")


@auth_bp.route("/connexion", methods=["GET", "POST"])
def connexion():
    if "mail" in session: #déjà connecté
        flash("Sign out to sign in to another account")
        redirect(url_for("gen_bp.acceuil"))
    if request.method == "POST":
        #gestion du formulaire saisi par l'utilisateur
        entree = request.form
        entreemail = entree['mail']
        entreemdp = entree['mdp']
        if valider_connexion(entreemail, entreemdp):
            session["mail"] = entreemail
            session["co"] = "Oui"
            return redirect(url_for("gen_bp.acceuil"))
        flash("Invalid email or password")
    return render_template("auth_connexion.html", session=session)


@auth_bp.route("/deconnexion")
def deconnexion():
    session.pop("mail") # on supprime id de l'objet session
    flash("You have successfully logged out")
    return redirect(url_for("gen_bp.home"))
