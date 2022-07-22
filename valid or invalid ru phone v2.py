number = 0
while number != "стоп":
    number = input("Введите номер телефона\n")
    if number.isnumeric():
        if number[0:2] == "79" or number[0:2] == "89":
            num = int(number)
            sum = 0
            while num != 0:
                sum += 1
                num = num // 10
            if sum == 11:
                print("Номер действителен")
        else:
            print("Номер недействителен")
    else:
        print("Номер недействителен")