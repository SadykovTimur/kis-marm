import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.auth_sudir_page import AuthSudirPage
from dit.qa.pages.main_page import MainPage
from dit.qa.pages.start_page import StartPage
from dit.qa.pages.sudir_page import SudirPage

__all__ = [
    'open_start_page',
    'open_test_start_page',
    'open_authorization_sudir_page',
    'sign_in',
    'sign_in_sudir',
    'open_main_page',
    'open_sudir_page',
    'open_directory',
    'add_directory',
    'delete_directory',
    'open_data_base',
    'add_table_data_base',
    'delete_table_data_base',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise e


def open_test_start_page(app: Application) -> None:
    with allure.step('Opening Test start page'):
        try:
            page = StartPage(app)
            page.base_url = 'https://test-kis-marm.mos.ru/login'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'test_start_page')
        except Exception as e:
            screenshot_attach(app, 'test_start_page_error')

            raise e


def open_authorization_sudir_page(app: Application) -> None:
    with allure.step('Opening Authorization sudir page'):
        try:
            page = StartPage(app)
            page.sudir.click()

            AuthSudirPage(app).wait_for_loading()

            screenshot_attach(app, 'authorization_sudir_page')
        except Exception as e:
            screenshot_attach(app, 'authorization_sudir_page_error')

            raise e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app)

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        auth_form.submit.click()


def sign_in_sudir(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = AuthSudirPage(app)

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        auth_form.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            MainPage(app).wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise e


def open_sudir_page(app: Application) -> None:
    with allure.step('Opening Sudir page'):
        try:
            SudirPage(app).wait_for_loading()

            screenshot_attach(app, 'sudir_page')
        except Exception as e:
            screenshot_attach(app, 'sudir_page_error')

            raise e


def open_directory(app: Application) -> None:
    with allure.step('Opening Directory'):
        try:
            page = MainPage(app)
            page.menu.directory.click()

            page.wait_directory()

            screenshot_attach(app, 'directory')
        except Exception as e:
            screenshot_attach(app, 'directory_error')

            raise e


def add_directory(app: Application, name: str = "monitoring", fields: str = "monitoring") -> None:
    with allure.step('Adding Directory'):
        try:
            page = MainPage(app)
            page.main.add.click()
            page.main.name.send_keys(name)
            page.main.add_field.click()
            page.main.fields.send_keys(fields)
            page.main.submit.click()

            page.add_directory()

            screenshot_attach(app, 'directory')
        except Exception as e:
            screenshot_attach(app, 'directory_error')

            raise e


def delete_directory(app: Application) -> None:
    with allure.step('Deleting Directory'):
        try:
            page = MainPage(app)
            page.main.delete[3].webelement.click()
            page.main.delete_record.click()

            page.delete_directory()

            screenshot_attach(app, 'directory')
        except Exception as e:
            screenshot_attach(app, 'directory_error')

            raise e


def open_data_base(app: Application) -> None:
    with allure.step('Opening Data base'):
        try:
            page = MainPage(app)
            page.menu.data_base.click()

            page.wait_data_base()

            screenshot_attach(app, 'data_base')
        except Exception as e:
            screenshot_attach(app, 'data_base_error')

            raise e


def add_table_data_base(app: Application, name: str = "monitoring", fields: str = "monitoring") -> None:
    with allure.step('Adding Table data base'):
        try:
            page = MainPage(app)
            page.main.add.click()
            page.main.name_bd.send_keys(name)
            page.main.add_column.click()
            page.main.fields_bd.send_keys(fields)
            page.main.submit.click()

            page.wait_table_data_base()

            screenshot_attach(app, 'table_data_base')
        except Exception as e:
            screenshot_attach(app, 'table_data_base_error')

            raise e


def delete_table_data_base(app: Application) -> None:
    with allure.step('Deleting Table data base'):
        try:
            page = MainPage(app)
            page.main.delete[1].webelement.click()
            page.main.delete_record.click()

            page.delete_table_data_base()

            screenshot_attach(app, 'table_data_base')
        except Exception as e:
            screenshot_attach(app, 'table_data_base_error')

            raise e
