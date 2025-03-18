import random
from datetime import datetime
import math


def generate_random_number():
    random_number = random.randint(1, 100)
    print(f"Случайное число от 1 до 100: {random_number}")


def print_current_datetime():
    current_datetime = datetime.now()
    print(f"Текущая дата и время: {current_datetime}")


def calculate_square_root_without_math(number):
    if number < 0:
        print("Невозможно вычислить квадратный корень из отрицательного числа.")
        return
    square_root = number ** 0.5
    print(f"Квадратный корень числа {number} (без использования модуля math): {square_root}")


def calculate_square_root_with_math(number):
    if number < 0:
        print("Невозможно вычислить квадратный корень из отрицательного числа.")
        return
    square_root = math.sqrt(number)
    print(f"Квадратный корень числа {number} (с использованием модуля math): {square_root}")


generate_random_number()
print_current_datetime()
calculate_square_root_with_math(25)
calculate_square_root_without_math(25)
