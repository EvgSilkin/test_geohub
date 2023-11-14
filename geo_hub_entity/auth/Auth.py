from utils.http_methods import HttpMethods
from keycloak import keycloak

class Auth:

    def __init__(self, keycloak: keycloak):
        self.keycloak = keycloak

    def send(self):
        response = HttpMethods.post(self.keycloak.get_url(),
                                    self.keycloak.get_headers(),
                                    self.keycloak.get_body())
        return response
