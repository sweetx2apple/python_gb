#Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
#income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return (f'{self.name} {self.surname}')

    def get_total_income(self):
        return int(self._income['wage']) + int(self._income['bonus'])


CEO = Position(name='Oleg', surname='Tinkov', position='ceo', income={'wage': 99999999, 'bonus': 11111111})
print(CEO.get_total_income())
print(CEO.get_full_name())