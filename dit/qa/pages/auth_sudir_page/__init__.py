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
    title = Text(class_name="page-title")
    login = TextField(id="login")
    password = TextField(id="password")
    submit = Button(id="bind")
    recovery_password = Component(id="recoveryEnter")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title == 'Вход в КИС МАРМ (ТЕСТ)'
                assert self.login.visible
                assert self.password.visible
                assert self.recovery_password.visible

                return self.submit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Страница авторицации СУДИР не загружена')
        self.app.restore_implicitly_wait()
