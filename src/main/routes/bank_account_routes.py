from flask import Blueprint, jsonify, request

from ...errors.error_handler import handler_errors
from ...views.http_types.http_request import HttpRequest
from ..composer.balance_editor_composer import balance_editor_composer
from ..composer.login_creator_composer import login_creator_composer
from ..composer.user_register_composer import user_register_composer
from ..middlewares.auth_jwt import auth_jwt_verify

bank_routes_bp = Blueprint("bank_routes", __name__)


@bank_routes_bp.route("/bank/registry", methods=["POST"])
def registry_user():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = user_register_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@bank_routes_bp.route("/bank/login", methods=["POST"])
def create_login():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = login_creator_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@bank_routes_bp.route("/bank/balance/<user_id>", methods=["PATCH"])
def edit_balance(user_id):
    try:
        token_informations = auth_jwt_verify()
        http_request = HttpRequest(
            body=request.json,
            params={"user_id": user_id},
            token_infos=token_informations,
        )
        http_response = balance_editor_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_errors(exception)
        return jsonify(http_response.body), http_response.status_code
