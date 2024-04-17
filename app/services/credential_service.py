from ..models.credential import Credential

credentials = []

def create_credential (did, role, alias, seed, verkey):
    credential = Credential(did, role, alias, seed, verkey)
    credentials.append(credential)
    return credential

def get_credentials():
    return credentials

def get_credentials_by_did(did):
    for credential in credentials:
        if credential.did == did:
            return credential
        return None
    