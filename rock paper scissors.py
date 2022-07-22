import random
print("Игра камень-ножницы-бумага")
variable = ["Камень", "Ножницы", "Бумага"]
sms = ""
while sms != "Стоп":
    sms = input("Выбор за вами\n")
    compsms = random.choice(variable)
    print("Компьютер выбрал", compsms)
    if sms.lower() == compsms.lower():
        print("Ничья")
    elif sms.lower() == "камень":
        if compsms == "Ножницы":
            print("Вы победили")
        elif compsms == "Бумага":
            print("Вы проиграли")
    elif sms.lower() == "бумага":
        if compsms == "Камень":
            print("Вы победили")
        elif compsms == "Ножницы":
            print("Вы проиграли")
    elif sms.lower() == "ножницы":
        if compsms == "Бумага":
            print("Вы победили")
        elif compsms == "Камень":
            print("Вы проиграли")