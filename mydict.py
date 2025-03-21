# Создаем словарь с информацией о студенте
student = {
    "имя": "Иван",
    "возраст": 20,
    "курс": 2
}

# Выводим информацию о студенте
print("Информация о студенте:")
print("Имя:", student["имя"])
print("Возраст:", student["возраст"])
print("Курс:", student["курс"])

# Создаем два словаря
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Объединяем словари
combined_dict = {**dict1, **dict2}

# Выводим объединенный словарь
print("Объединенный словарь:", combined_dict)

# Создаем словарь
student = {
    "имя": "Иван",
    "возраст": 20,
    "курс": 2
}

# Ключ, который нужно проверить
key_to_check = "возраст"

# Проверяем, есть ли ключ в словаре
if key_to_check in student:
    print(f"Ключ '{key_to_check}' найден в словаре.")
else:
    print(f"Ключ '{key_to_check}' не найден в словаре.")