from random import randint
print("Игра в кости")
answer = ""
while 1:
    answer = input("Бросить кости? (Да/Нет)\n")
    if answer.lower() == "да":
        comp = randint(1, 6)
        user = randint(1, 6)
        print("У вас выпало", user)
        print("Компьютеру выпало", comp)
        if comp == user:
            print("Ничья")
        elif comp > user:
            print("Вы проиграли")
        elif user > comp:
            print("Вы победили")
    elif answer.lower() == "нет":
        break
    else:
        print("Неверная команда")
