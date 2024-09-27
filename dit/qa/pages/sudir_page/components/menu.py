from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    user = Component(xpath='//span[text()="Сухарев Е. Р."]')
    monitoring = Component(xpath='//span[text()="Мониторинг"]')
    users = Button(xpath='//span[text()="Внешние пользователи"]')
    recovery_pass = Component(xpath='//span[text()="Восстановление пароля"]')
    directory = Component(xpath='//span[text()="Справочники"]')
    messages = Component(xpath='//span[text()="Обмен сообщениями"]')
    info_message = Component(xpath='//span[text()="Информационные сообщения"]')
    statistics = Component(xpath='//span[text()="Статистика"]')

    @property
    def is_visible(self) -> bool:
        assert self.user.visible
        assert self.monitoring.visible
        assert self.users.visible
        assert self.recovery_pass.visible
        assert self.messages.visible
        assert self.info_message.visible
        assert self.statistics.visible

        return self.directory.visible


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
