def zzz(sms1):
    sms = sms1
    sms = sms.replace('а', 'ё')
    sms = sms.replace('б', '.')
    sms = sms.replace('в', '0')
    sms = sms.replace('г', '9')
    sms = sms.replace('д', '8')
    sms = sms.replace('е', '7')
    sms = sms.replace('ё', '6')
    sms = sms.replace('ж', '5')
    sms = sms.replace('з', '4')
    sms = sms.replace('и', '3')
    sms = sms.replace('й', '2')
    sms = sms.replace('к', '1')
    sms = sms.replace('л', '!')
    sms = sms.replace('м', '@')
    sms = sms.replace('н', '#')
    sms = sms.replace('о', '$')
    sms = sms.replace('п', '%')
    sms = sms.replace('р', '^')
    sms = sms.replace('с', '&')
    sms = sms.replace('т', '*')
    sms = sms.replace('у', '(')
    sms = sms.replace('ф', ')')
    sms = sms.replace('х', '-')
    sms = sms.replace('ц', '_')
    sms = sms.replace('ч', '=')
    sms = sms.replace('ш', '+')
    sms = sms.replace('щ', '/')
    sms = sms.replace('ь', '|')
    sms = sms.replace('ы', '{')
    sms = sms.replace('ъ', '}')
    sms = sms.replace('э', '<')
    sms = sms.replace('ю', '[')
    sms = sms.replace('я', ']')
    sms = sms.replace('a', '>')
    sms = sms.replace('b', ',')
    sms = sms.replace('c', '~')
    sms = sms.replace('d', '`')
    sms = sms.replace('e', 'п')
    sms = sms.replace('f', 'в')
    sms = sms.replace('g', 'ц')
    sms = sms.replace('h', 'й')
    sms = sms.replace('i', 'ф')
    sms = sms.replace('j', 'ы')
    sms = sms.replace('k', 'ч')
    sms = sms.replace('l', 'я')
    sms = sms.replace('m', 'и')
    sms = sms.replace('n', 'т')
    sms = sms.replace('o', 'ь')
    sms = sms.replace('p', 'д')
    sms = sms.replace('q', 'g')
    sms = sms.replace('r', 'h')
    sms = sms.replace('s', 'f')
    sms = sms.replace('t', 'd')
    sms = sms.replace('u', 's')
    sms = sms.replace('v', 'a')
    sms = sms.replace('w', 'z')
    sms = sms.replace('x', 'o')
    sms = sms.replace('y', 'p')
    sms = sms.replace('z', 'x')
    print(f"Итог:\n {sms}")

while 1:
    text = input("Введите текст для шифрования")
    text = zzz(text)