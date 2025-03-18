def calculate(expression):
    try:
        result = eval(expression)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}. Пожалуйста, введите корректное выражение.")

def main():
    user_input = input("Введите арифметическое выражение (например, 2 + 2): ")
    calculate(user_input)


if __name__ == "__main__":
    main()
