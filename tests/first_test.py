import allure

from users.user_map_owner import UserMapOwner

owner_login = "geohub.test@gmail.com"
owner_password = "geohub.test"

@allure.description("Формулировка теста")
def test_auth():
    user_map_owner = UserMapOwner(owner_login, owner_password)
    response = user_map_owner.auth()
    print(response)

