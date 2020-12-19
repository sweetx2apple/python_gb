#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

#def function(first_name: str, last_name: str, birth_year: str, city: str, email: str, phone: str) -> str:
#а змеюка так понимает? как выше...или это чисто для себя удобная логика и потереть?

def function(first_name, last_name, birth_year, city, email, phone):
    return print(f'{first_name} {last_name}, {birth_year}, {city}, {email}, {phone}')

#def function(first_name, last_name, birth_year, city, email, phone,**kwargs):