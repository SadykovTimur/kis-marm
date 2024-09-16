from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['AuthSudirPage']


class AuthSudirPage(Page):
    title = Text(tag="h1")
    login = TextField(name="login")
    password = TextField(name="password")
    submit = Button(xpath='//span[text()="Войти"]')
    recovery_password = Component(xpath='//a[text()="Восстановить пароль"]')
    sudir = Button(xpath='//a[text()="Войти через СУДИР"]')
    user_fkr = Component(xpath='//a[text()="Вход для руководителя ФКР"]')
    user_sgtn = Component(xpath='//a[text()="Вход для руководителя СГТН"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title == 'КИС'
                assert self.login.visible
                assert self.password.visible
                assert self.recovery_password.visible
                assert self.sudir.visible
                assert self.user_sgtn.visible
                assert self.user_fkr.visible

                return self.submit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=35, msg='Стартовая страница не загружена')
        self.app.restore_implicitly_wait()
