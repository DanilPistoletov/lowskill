logpass = {}
mailbox = {}

def action1():
    action = input("1 - регистрация, 2 - авторизация")
    if action == "1":
        login = input("Введите логин")
        while len(login) < 3:
            login = input("Логин должен быть больше 2 символов")
        passw = input("Введите пароль")
        while len(passw) < 6:
            passw = input("Пароль должен быть больше 5 символов")
        print("Регистрация пройдена успешно")
        logpass[login] = passw
        return action1()
    elif action == "2":
        logintry = input("Введите логин")
        while logintry in logpass.values() == 0:
            logintry = input("Неверный логин")
        passwtry = input("Введите пароль")
        while passwtry != logpass[logintry]:
            passwtry = input("Неверный пароль")
        global truelogin
        global truepassw
        truelogin = logintry
        truepassw = passwtry
        print("Успешный вход")

action1()

while 1:
    action = input("1 - проверка почты, 2 - отправка почты")
    if action == "1":
        sms = mailbox.get(truelogin)
        if sms is None:
            print("Сообщений не найдено")
        else:
            print(sms)
    elif action == "2":
        smslogin = input("Введите логин получателя")
        while len(smslogin) < 3:
            smslogin = input("Логин получателя должен быть больше 2 символов")
        smstext = input("Введите текст сообщения")
        while len(smstext) < 1:
            smstext = input("Сообщение должно содержать минимум 1 символ")
        mailbox[smslogin] = smstext