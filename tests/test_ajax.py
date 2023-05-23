from flask import url_for
from http import HTTPStatus
import json

def test_active_ventilo(client):
    a= client.post(
        url_for("gen_bp.gererventilo"),
        data=json.dumps({"value": "ON"}),
        content_type="application/json",
    )