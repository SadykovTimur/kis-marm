import allure
from _pytest.fixtures import FixtureRequest

from tests.api.steps import api_auth, get_pattern, get_pattern_docx


@allure.epic('KIS-MARM')
@allure.title('Печать шаблонов')
def test_print_pattern(request: FixtureRequest) -> None:
    token = api_auth(request.config.option.username, request.config.option.password)

    get_pattern(token)
    get_pattern_docx(token)
