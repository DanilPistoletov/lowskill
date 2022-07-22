number = input("Введите номер телефона")
check = 0

#Проверка №1
if number.isnumeric():
    check += 1
else:
    check -= 1

#Проверка №2
if number[0:2] == "79" or number[0:2] == "89":
    check += 1
else:
    check -= 1

#Проверка №3
num = int(number)
sum = 0
while num != 0:
    sum += 1
    num = num // 10
if sum == 11:
    check += 1
else:
    check -= 1

#Итоговый подсчёт
if check == 3:
    print("Номер действителен")
else:
    print("Номер недействителен")