from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    add_table_data_base,
    delete_table_data_base,
    open_data_base,
    open_main_page,
    open_start_page,
    sign_in,
)


@allure.epic('KIS-MARM')
@allure.title('Добавление таблицы БД')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_add_data_base(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    open_start_page(app)
    sign_in(app, request.config.option.username, request.config.option.password)

    open_main_page(app)

    open_data_base(app)
    add_table_data_base(app)
    delete_table_data_base(app)
