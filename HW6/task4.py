# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

import random


class Car(object):
    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = None
        self.current_speed = 0

    def show_speed(self):
        if self.current_speed == 0:
            print(f'standing still, but max speed is {self.speed}')
        else:
            return self.current_speed

    def go(self):
        self.current_speed = random.randrange(0, self.speed, 1)
        print(f'going with the speed of {self.current_speed}')

    def stop(self):
        self.current_speed = 0
        print('stopped')

    def turn(direction: str):
        if direction in ["right", "left", "north", "south", "west", "east", "around"]:
            print(f'turning {direction}')
        else:
            print('command ignored')


class TownCar(Car):
    def show_speed(self):
        if self.current_speed == 0:
            print(f'standing still, but max speed is {self.speed}')
        else:
            return self.current_speed if self.current_speed < 60 else print('Moving too fast!')


class WorkCar(Car):
    def show_speed(self):
        if self.current_speed == 0:
            print(f'standing still, but max speed is {self.speed}')
        else:
            return self.current_speed if self.current_speed < 40 else print('Moving too fast!')


class SportCar(Car):
    #''''''
    def show_speed(self):
        if self.current_speed == 0:
           print(f'standing still, but max speed is {self.speed}')
        else:
            return self.current_speed if self.current_speed > 100 else print('Moving too slow!')

class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True
        self.current_speed = 0


class Taxi(Car):
    print('TAXI')