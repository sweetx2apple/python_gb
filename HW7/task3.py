# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

#Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
#Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
# количества ячеек этих двух клеток.
#Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
#количества ячеек этих двух клеток.
#В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
#Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
#Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell(object):
    def __init__(self, a: int, ):
        self.cells = a

    def __add__(self, other):
        if isinstance(other, Cell):
            self.cells += other.cells
            return self.cells
        else:
            raise TypeError('норм чё))') #неправильный тип второго операнда、уотакуот

    def __sub__(self, other):
        if self.cells - other.cells < 0:
            print('найс трай))')
            return (0)
        else:
            self.cells -= other.cells
            return self.cells

    # return Cell(self.cells+other.cells)
    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.cells * other.cells)
        else:
            raise TypeError('норм чё))')

    def __truediv__(self, other):
        if isinstance(other, Cell):
            d = self.cells / other.cells
            return Cell(int(d))
        else:
            raise TypeError('愚か者')
        # return (Cell(1))

    def make_order(self, row):
        s = ''
        if row > 0 and not row > self.cells:
            if row == 1:
                for each in range(0, self.cells):
                    s += '*'
                return s + "\n"
            else:
                c = self.cells
                for each in range(c, 0, -1):
                    while c >= row:
                        for l in range(0, row):
                            s += '*'
                            c = c - 1
                        s += "\n"
                    if c > 0 and c < row:
                        for i in range(c, 0, -1):
                            s += '*'
                        s += "\n"
                    elif c == row:
                        for i in range(0, row):
                            s += '*'
                        return s + "\n"
                    return s
                return s
        else:
            s = "найс количество ячеек в ряду))"
            return s


# (ಥ﹏ಥ) мозгодробительная штуковина (ಥ﹏ಥ)
# даже нет желания орать, как я обычно это делаю в комментах...