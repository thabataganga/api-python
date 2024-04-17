from flask import jsonify, request
from ..services.credential_service import *

def create_credential_controller(): 
    data = request.json
    did = data.get("did")
    role = data.get("role")
    alias = data.get("alias")
    seed = data.get("seed")
    verkey = data.get("verkey")
    credential = create_credential(did, role, alias, seed, verkey)
    return jsonify({"did": credential.did, "role": credential.role, "alias": credential.alias, "seed": credential.seed, "verkey": credential.verkey}), 201

def get_credentials_controller():
    credentials = get_credentials()
    credentials_data = [{"did": credential.did, "role": credential.role, "alias": credential.alias, "seed": credential.seed, "verkey": credential.verkey} for credential in credentials]
    return jsonify(credentials_data)

def get_credential_by_did_controller(did):
    credential = get_credentials_by_did(did)
    if credential:
        return jsonify({"did": credential.did, "role": credential.role, "alias": credential.alias, "seed": credential.seed, "verkey": credential.verkey})
    else:
        return jsonify([{"error": "Credential nof found"}]), 404