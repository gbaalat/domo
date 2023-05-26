from flask import url_for
from http import HTTPStatus
import json

def test_active_ventilo(client):
    a= client.get(
        url_for("auth_bp.connexion")
    )