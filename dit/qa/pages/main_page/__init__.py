from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.components.main import Main
from dit.qa.pages.main_page.components.menu import Menu

__all__ = ['MainPage']


class MainPage(Page):
    menu = Menu(css='[class*="DockedLeft"]')
    main = Main(tag="main")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.main.title == '  Информационная панель'

                return self.menu.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=35, msg='Главная страница не отображена')
        self.app.restore_implicitly_wait()

    def wait_directory(self) -> None:
        def condition() -> bool:
            try:
                assert self.main.directory.visible
                assert self.main.aus.visible
                assert self.main.gis.visible

                return self.main.root[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=35, msg='Меню "Справочники" не загружена')
        self.app.restore_implicitly_wait()

    def add_directory(self) -> None:
        def condition() -> bool:
            try:
                assert self.main.message == 'Запись успешно добавлена.'

                return self.main.monitoring.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Справочник не создан')
        self.app.restore_implicitly_wait()

    def delete_directory(self) -> None:
        def condition() -> bool:
            try:
                return self.main.message == 'Запись успешно удалена.'

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Справочни не удален')
        self.app.restore_implicitly_wait()

    def wait_data_base(self) -> None:
        def condition() -> bool:
            try:
                return self.main.data_base.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=35, msg='Меню "База данных" не загружена')
        self.app.restore_implicitly_wait()

    def wait_table_data_base(self) -> None:
        def condition() -> bool:
            try:
                assert self.main.message == 'Запись успешно добавлена.'

                return self.main.monitoring.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Таблица не создана')
        self.app.restore_implicitly_wait()

    def delete_table_data_base(self) -> None:
        def condition() -> bool:
            try:
                return self.main.message == 'Запись успешно удалена.'

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Таблица не удалена')
        self.app.restore_implicitly_wait()
