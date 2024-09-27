from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.sudir_page.components.menu import Menu

__all__ = ['SudirPage']


class SudirPage(Page):
    menu = Menu(css='[class*="DockedLeft"]')
    title = Text(tag='h1')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title == '  Информационная панель'

                return self.menu.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=35, msg='Главная страница не отображена')
        self.app.restore_implicitly_wait()
