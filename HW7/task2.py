#Реализовать проект расчета суммарного расхода ткани на производство одежды.
#Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#К типам одежды в этом проекте относятся пальто и костюм.
#У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
#Это могут быть обычные числа: V и H, соответственно.


#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
#для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
#реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothing(object):
    def __init__(self):
        self._cloth_amount = None
        pass

    cloth_amount = property()

    @cloth_amount.setter
    def cloth_amount(self, A):
        if A < 0:
            self._cloth_amount = 0
        else:
            if self._H:
                self._cloth_amount = float(2*A + 0.3)
            else:
                self._cloth_amount = float(A/6.5 + 0.5)

    @cloth_amount.getter
    def cloth_amount(self):
        return self._cloth_amount

class Coat(Clothing):
    def __init__(self):
        self._H = True
        self._F = None
        self._cloth_amount = None

class Suit(Clothing):
    def __init__(self):
        self._V = True
        self._H = None
        self._cloth_amount = None

a = Suit()
a.cloth_amount = 10
b = Coat()
b.cloth_amount = 10
print ('suit: '+str(a.cloth_amount))
print ('coat: '+str(b.cloth_amount))

#(ಠ_ಠ）┳━┳ ╮°-°)╮ ┳━┳ (ノಠ益ಠ)ノ彡┻━┻