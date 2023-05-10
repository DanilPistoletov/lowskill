#Проверка длины ника до 20 символов
text = input("Введите ник до 20 символов")
if len(text) < 20:
    print("Успешно")
else:
    print("Ник больше 20 символов")

#Проверка длины ника больше 3 символов
text = input("Введите ник не короче 3 символов")
if len(text) < 3:
    print("Ник короче 3 символов")
else:
    print("Успешно")

#Проверка по минимальной и максимальной длине
text = input("Введите ник не короче 3 символов и не длиннее 20")
if len(text) < 21:
    if len(text) > 2:
        print("Успешно")
    else:
        print("Ник короче 3 символов")
else:
    print("Ник длиннее 20 символов")

#Проверка сложности пароля по количеству символов, наличию цифр и символов
password = input("Введите пароль")
numcheck = 0
symcheck = 0
a = 0
b = 0
c = 0
if len(password) > 6:
    a = 1
for i in password:
    if i in "1234567890":
        numcheck += 1
if numcheck > 2:
    b = 1
for i in password:
    if i in "!@#$%&*":
        symcheck += 1
if symcheck > 1:
    c = 1
if a & b & c == 1:
    print("Надёжный пароль")
elif a or b or c == 1:
    print("Ненадёжный пароль")