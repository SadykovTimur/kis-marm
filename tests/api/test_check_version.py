import allure
from _pytest.fixtures import FixtureRequest

from tests.api.steps import api_auth, check_actual_version, check_old_version, get_apk_files


@allure.epic('KIS-MARM')
@allure.title('Проверка версии')
def test_check_version(request: FixtureRequest) -> None:
    token = api_auth(request.config.option.username, request.config.option.password)

    check_actual_version(token)

    check_old_version(token)

    get_apk_files()
