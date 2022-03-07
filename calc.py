a = float(input("Введите число\n"))
while True:
	b = input("Введите действие\n")
	c = float(input("Введите другое число\n"))
	if b == "*":
		a = a*c
	elif b == "+":
		a=a+c
	elif b == "/":
		a=a/c
	elif b == "-":
		a=a-c
	elif b == "^":
		a=a**c
	elif b == "√":
		a=a**(1/c)
		a=round(a)
	elif b == "%":
		a=a/100*c
	print("Получилось", a)