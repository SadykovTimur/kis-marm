import allure

from tests.api.steps import check_apps


@allure.epic('KIS-MARM')
@allure.title('Диагностика')
def test_check_app() -> None:
    check_apps()
