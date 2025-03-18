def get_number_from_user():
    try:
        number = float(input("Введите число: "))
        print(f"Вы ввели число: {number}")
    except ValueError:
        print("Ошибка: введено не число. Пожалуйста, введите корректное число.")

get_number_from_user()

def open_file_safely(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Содержимое файла {filename}:\n{content}")
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")

open_file_safely('exple.txt')

get_number_from_user()

open_file_safely('example.txt')