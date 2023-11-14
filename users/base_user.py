from geo_hub_entity.auth.Auth import Auth
from keycloak.keycloak import KeyCloak

class BaseUser:

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._access_token = ""
        self._refresh_token = ""

    def get_login(self):
        return self._login

    def get_password(self):
        return self._password

    def get_access_token(self):
        return self._access_token

    def get_refresh_token(self):
        return self._refresh_token

    def set_access_token(self, access_token):
        self._access_token = access_token

    def set_refresh_token(self, refresh_token):
        self._refresh_token = refresh_token

    def _init_keycloak(self):
        keycloak = KeyCloak(self._login, self._password)
        return keycloak

    def auth(self):
        keycloak = self._init_keycloak()
        auth = Auth(keycloak)
        response = auth.send()
        return response

