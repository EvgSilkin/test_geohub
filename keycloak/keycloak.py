


#ВЫНЕСТИ СЕКРЕТНЫЙ ТОКЕН В ENV


class KeyCloak:

    def __init__(self, login, password):
        self._url = "https://keycloak-dev.geocode.tech/realms/geocode/protocol/openid-connect/token"
        self._client_secret = "m7N6osjblD4LyZquTFtGARapwHrDa2m7"
        self._headers = {
            "Content-Type":"application/x-www-form-urlencoded"
        }
        self._body = {
            "grant_type": "password",
            "username": login,
            "password": password,
            "client_id": "account",
            "client_secret": self._client_secret
        }

    def get_url(self):
        return self._url

    def get_headers(self):
        return self._headers

    def get_body(self):
        return self._body
