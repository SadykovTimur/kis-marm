from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import open_authorization_sudir_page, open_sudir_page, open_test_start_page, sign_in_sudir


@allure.epic('KIS-MARM')
@allure.title('Интеграция с СУДИР')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_integration_sudir(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    open_test_start_page(app)

    open_authorization_sudir_page(app)

    sign_in_sudir(app, request.config.option.username_sudir, request.config.option.password_sudir)

    open_sudir_page(app)
