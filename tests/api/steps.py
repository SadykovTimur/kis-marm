import allure

from dit.qa.api.auth import auth

__all__ = ['api_auth']


def api_auth(login: str, password: str) -> str:
    with allure.step(f'API authorization by {login}'):
        code, token = auth(login, password)

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"

        return token
