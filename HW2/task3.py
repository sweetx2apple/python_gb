#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.

seasons = {
    '1': "Зима",
    '2': "Зима",
    '3': "Весна",
    '4': "Весна",
    '5': "Весна",
    '6': "Лето",
    '7': "Лето",
    '8': "Лето",
    '9': "Осень",
    '10': "Осень",
    '11': "Осень",
    '12': "Зима"
}
month_num = input("Введите число от 1 до 12: ")
for s in seasons:
    if month_num in s:
        print(seasons[s])
  # else:
  #      print("Сказали же, от 1 до 12, ну")


#lis_s = ["Зима", "Весна", "Лето", "Осень"]
#lis_pos = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]

#num = int(input("2. Enter number from 1 to 12: "))

#for index, l in enumerate(lis_pos):
#    if num in l:
#        print(lis_s[index])