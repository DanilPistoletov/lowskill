from random import randint
print("Игра угадай число от 1 до 7")
sms = ""
while 1:
    sms = int(input("Введите число\n"))
    number = randint(1, 7)
    if sms == number:
        print("Вы угадали")
    else:
        print("Вы не смогли угадать")