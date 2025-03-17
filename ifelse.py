number = int(input("Введите число: "))
if number % 2 == 0:
    print(f"Число {number} является четным.")
else:
    print(f"Число {number} является нечетным.")

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if num1 > num2:
    print(f"Наибольшее число: {num1}")
elif num2 > num1:
    print(f"Наибольшее число: {num2}")
else:
    print("Оба числа равны.")

age = int(input("Введите ваш возраст: "))
if age >= 18:
    print("Вы можете получить водительские права.")
else:
    print("Вы не можете получить водительские права.")