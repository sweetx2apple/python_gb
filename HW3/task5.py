#Программа запрашивает у пользователя строку чисел, разделенных пробелом.
#При нажатии Enter должна выводиться сумма чисел.
#Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
#Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается.
#Если специальный символ введен после нескольких чисел,
#то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

#symbol = input("Введите стоп-символ: ")[0]
#row=''
#def f(s,l):
#    x=0
#    for i in l:
#        if i == symbol:
#            exit()
#        x+=int(i)
#    return s + x

#s=0
#if __name__ == "__main__":
#    while not None:
#        row=input("Исчо: ").split()
#        s = f(s,row)
#        print(s)

#ух тут секса привалило на пол года вперед, не знаю как у других
#думала про кучу елдов, но чет это вообще порно на ножках выходило

#symbol = input("stop at: ")
#row=''
#s=0

#def sum(s,l):
#    x = 0
#    for i in l:
#        if i == symbol:
#            print (s + x)
#            exit()
#        x += int(i)
#    return s + x

#if __name__ == "__main__":
#    while True:
#        row=input("input: ")
#        s = sum(s,row.split())
#        print (s)

#ValueError ещё воткнуть..или не надо..или надо..3-06 ночи,а у меня дисперсия 800 Т_Т
#AAAAAAaaaaaaaaaaaaaaaaaaaaaaaa
symbol = ''
while symbol.isalpha() is not True:
    symbol = input("Стоп символ (не цифры, буковки дауай): ")[0]
row=''
s=0

def sum(s,l):
    x = 0
    for i in l:
        if i == symbol:
            print (s + x)
            exit()
        try:
            x += int(i)
        except ValueError:
            print (s + x)
            exit()
    return s + x

if __name__ == "__main__":
    while True:
        row=input("input: ")
        s = sum(s,row.split())
        print (s)
#ideal version です。