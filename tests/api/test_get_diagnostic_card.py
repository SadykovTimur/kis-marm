import allure

from tests.api.steps import get_json_dk, version_dk


@allure.epic('KIS-MARM')
@allure.title('Получение Диагностической карты')
def test_get_diagnostic_card() -> None:
    version_dk()
    get_json_dk()
