import allure
from _pytest.fixtures import FixtureRequest

from tests.api.steps import api_auth


@allure.epic('KIS-MARM')
@allure.title('Аутентификация пользователя')
def test_check_api_auth(request: FixtureRequest) -> None:

    api_auth(request.config.option.username, request.config.option.password)
