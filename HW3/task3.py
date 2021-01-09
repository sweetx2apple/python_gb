#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    l = sorted([arg1, arg2, arg3], key=int, reverse=True)
    return l[0]+l[1]

#может и не инты искать, конечно...
#разврааат головного мооозгааа
#    return sorted([arg1, arg2, arg3], key=int, reverse=True)[0] + sorted([arg1, arg2, arg3], key=int, reverse=True)[1]