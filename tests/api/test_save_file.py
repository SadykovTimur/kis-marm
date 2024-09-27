import allure
from _pytest.fixtures import FixtureRequest

from tests.api.steps import api_auth, check_files, delete_files, deleted_file, download_files, get_files, transfer_files


@allure.epic('KIS-MARM')
@allure.title('Хранение файлов')
def test_save_file(request: FixtureRequest) -> None:
    token = api_auth(request.config.option.username, request.config.option.password)

    check_files(token)
    delete_files(token)
    download_files(token)
    transfer_files(token)
    get_files(token)
    deleted_file(token)
