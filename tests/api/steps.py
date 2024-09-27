import allure

from dit.qa.api.auth import (
    actual_version,
    auth,
    check_app,
    check_file,
    delete_file,
    deleted_files,
    download_file,
    get_apk_file,
    get_file,
    get_json_file_dk,
    get_print_pattern,
    get_print_pattern_docx,
    get_version_dk,
    old_version,
    transfer_file,
)

__all__ = [
    'api_auth',
    'wrong_password',
    'check_apps',
    'check_actual_version',
    'get_apk_files',
    'version_dk',
    'get_json_dk',
    'check_files',
    'delete_files',
    'download_files',
    'transfer_files',
    'check_old_version',
    'get_files',
    'deleted_file',
    'get_pattern',
    'get_pattern_docx',
]


def api_auth(login: str, password: str) -> str:
    with allure.step(f'API authorization by {login}'):
        code, response = auth(login, password)

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"
        assert response['firstName'] == 'DIT'
        assert response['middleName'] == 'DIT'
        assert response['lastName'] == 'DIT'
        assert response['redirectToRoute'] == 'change_password'
        return response['token']


def wrong_password(login: str, password: str = 'xxxxxxxxx') -> None:
    with allure.step(f'Checking wrong password'):
        response = auth(login, password)

        assert response[1]['message'] == 'Неправильный логин или пароль'


def check_apps() -> None:
    with allure.step(f'Checking application performance'):
        code = check_app()

        assert code == 204, f"Код ответа {code} не соответствует ожидаемому"


def check_actual_version(token: str) -> None:
    with allure.step(f'Checking actual version'):
        code = actual_version(token)

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"


def check_old_version(token: str) -> None:
    with allure.step(f'Checking old version'):
        response = old_version(token)

        assert response['message'] == 'Устаревшая версия клиента'


def get_apk_files() -> None:
    with allure.step(f'Getting apk file'):
        code = get_apk_file()

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"


def version_dk() -> None:
    with allure.step(f'Getting version dk'):
        response = get_version_dk()

        assert response['version'] == 228


def get_json_dk() -> None:
    with allure.step(f'Getting dk file'):
        response = get_json_file_dk()

        assert response['controls'] != ''


def check_files(token: str) -> None:
    with allure.step(f'Checking file'):
        code = check_file(token)

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"


def delete_files(token: str) -> None:
    with allure.step(f'Deleting file'):
        code = delete_file(token)

        assert code == 204, f"Код ответа {code} не соответствует ожидаемому"


def download_files(token: str) -> None:
    with allure.step(f'Deleting file'):
        response = download_file(token)

        assert response['bytes'] == 0


def transfer_files(token: str) -> None:
    with allure.step(f'Transferring file'):
        code, response = transfer_file(token)

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"
        assert response['uuid'] != ''


def get_files(token: str) -> None:
    with allure.step(f'Getting files'):
        code = get_file(token)

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"


def deleted_file(token: str) -> None:
    with allure.step(f'Deleting files'):
        code = deleted_files(token)

        assert code == 204, f"Код ответа {code} не соответствует ожидаемому"


def get_pattern(token: str) -> None:
    with allure.step(f'Getting pattern'):
        response = get_print_pattern(token)

        assert response['data'][0]['name'] == 'СГТН. Диагностическая карта'


def get_pattern_docx(token: str) -> None:
    with allure.step(f'Getting pattern docx'):
        code = get_print_pattern_docx(token)

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"
