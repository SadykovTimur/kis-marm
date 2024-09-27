import allure
from _pytest.fixtures import FixtureRequest

from tests.api.steps import api_auth, wrong_password


@allure.epic('KIS-MARM')
@allure.title('Аутентификация пользователя')
def test_check_api_auth(request: FixtureRequest) -> None:
    api_auth(request.config.option.username, request.config.option.password)

    wrong_password(request.config.option.username, 'xxxxxxxxx')
