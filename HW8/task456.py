
class Kantoorapparatuur(object):
    def __init__(self):
        self.temp_memory = None

    def store(self, warenhuis):
        if isinstance(warenhuis, Warenhuis):
            warenhuis.store(self)
        else:
            print(f'{type(self)} можно хранить только в Warenhuis')


class Printer(Kantoorapparatuur):

    def do_printing(self, something):
        print(something)


class Scanner(Kantoorapparatuur):

    def scan(self, something):
        self.temp_memory = None
        if isinstance(something, (str, list, tuple, dict, int, float)):
            self.temp_memory = something
            return True
        else:
            print("Эт нельзя отсканить")
            return False

    def scan_n_print(self, something, printer: Printer):
        if isinstance(printer, Printer):
            if self.scan(something):
                printer.do_printing(something)
        else:
            print('Нужно подключить принтер...')


class Copier(Kantoorapparatuur):

    def copy(self, something):
        if isinstance(something, (set, list, dict)):
            self.temp_memory = something.copy()
            return self.temp_memory
        elif isinstance(something, (str, int, tuple)):
            self.temp_memory = something
            return self.temp_memory
        else:
            print('Это нельзя скопировать')


class Warenhuis(object):
    def __init__(self):
        self.__storage = [0, []]

    def print_contents(self):
        for i in range(0, self.__storage[0]):
            print(f'{i}, {self.__storage[1][i]}')

    def store(self, kantoorapparatuur):
        if isinstance(kantoorapparatuur, (Printer, Scanner, Copier))):
            self.__storage[0] += 1
            self.__storage[1].append(kantoorapparatuur)
        else:
            print(f'Этот склад ток для Kantoorapparatuur, а не для {type(kantoorapparatuur)}')

    def __add__(self, other):
        if isinstance(other, (Printer, Copier, Scanner)):
            self.__storage[0] += 1
            self.__storage[1].append(other)
            return self.__storage
        elif isinstance(other, Warenhuis):
            self.__storage[0] += other.__storage[0]
            for item in other.__storage[1]:
                self.__storage[1].append(item)
            return self.__storage
        else:
            raise TypeError