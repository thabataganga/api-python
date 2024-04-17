from flask import Blueprint
from .controllers.credential_controller import *

api_bp = Blueprint("api", __name__)

# Definindo um manipulador de solicitações para definir o Content-Type globalmente
@api_bp.before_request
def before_request():
    if request.method == 'POST' or request.method == 'PUT':
        content_type = request.headers.get('Content-Type', '')
        if content_type not in ['application/json']:
            return jsonify({'error': 'Content-Type must be application/json or multipart/form-data'}), 415

@api_bp.route('/', methods=['GET'])
def hello_world():
    msg = {"msg": "Welcome to the Non-Profit ID API!"}
    return jsonify(msg)

@api_bp.route('/new_credential', methods=['POST'])
def create_credential_route():
    return create_credential_controller()

@api_bp.route('/credentials', methods=['GET'])
def get_credentials_route():
    return get_credentials_controller()

@api_bp.route('/credentials/<int:did>', methods=['GET'])
def get_credential_by_did_route(did):
    return get_credential_by_did_controller(did)