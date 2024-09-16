from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField

__all__ = ['Main']


class MainWrapper(ComponentWrapper):
    title = Text(tag='h1')
    directory = Component(xpath='//th[text()="Название справочника"]')
    data_base = Component(xpath='//th[text()="Наименование таблицы"]')
    aus = Component(xpath='//span[text()="Перейти в АС УР"]')
    gis = Component(xpath='//span[text()="Перейти в ГИС ЕХД"]')
    root = Components(css='[class*="MuiFab-root"]')
    add = Button(css='[title="Добавить"]')
    add_field = Button(xpath='//label[text()="Поля"]/following:: button[@title="Добавить"]')
    add_column = Button(xpath='//label[text()="Столбцы"]/following:: ul/button')
    name = TextField(xpath='//label[text()="Название справочника"]/following:: input[@name="name"]')
    name_bd = TextField(xpath='//label[text()="Наименование"]/following:: input[@name="name"]')
    message = Text(css='[class*="message"]')
    monitoring = Component(xpath='//td[text()="monitoring"]')
    fields = TextField(xpath='//label[text()="Поля"]/following::input[@name="fields"]')
    fields_bd = TextField(xpath='//label[text()="Столбцы"]/following:: input[@placeholder="Наименование"] ')
    submit = Button(xpath='//span[text()="Применить"]')
    delete = Components(css='[class*="TableBody"] a')
    delete_record = Button(xpath='//span[text()="Удалить"]')


class Main(Component):
    def __get__(self, instance, owner) -> MainWrapper:
        return MainWrapper(instance.app, self.find(instance), self._locator)
