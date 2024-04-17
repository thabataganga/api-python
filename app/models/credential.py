class Credential:
    def __init__(self, did, role, alias, seed, verkey):
        self.did = did
        self.role = role
        self.alias = alias
        self.seed = seed
        self.verkey = verkey