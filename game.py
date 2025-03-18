import random

def guess_number_game():
    # Генерируем случайное число от 0 до 10
    target_number = random.randint(0, 10)
    attempts = 3

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 0 до 10. Попробуй угадать его за 3 попытки.")

    for attempt in range(attempts):
        try:
            guess = int(input(f"Попытка {attempt + 1}: Введите ваше предположение: "))

            if guess == target_number:
                print("Поздравляю! Вы угадали число!")
                return
            elif guess < target_number:
                print("Не верно! Загаданное число больше.")
            else:
                print("Не верно! Загаданное число меньше.")
        except ValueError:
            print("Ошибка: введено не число. Пожалуйста, введите корректное число.")

    print(f"К сожалению, вы не угадали число. Загаданное число было {target_number}.")

# Пример использования
if __name__ == "__main__":
    guess_number_game()
