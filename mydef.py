def sum_two_numbers(a, b):
    return a + b

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def average_of_list(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

result = sum_two_numbers(3, 5)
print(f"Сумма: {result}")

number = 11
if is_prime(number):
    print(f"{number} является простым числом.")
else:
    print(f"{number} не является простым числом.")

numbers_list = [1, 2, 3, 4, 5]
average = average_of_list(numbers_list)
print(f"Среднее значение: {average}")
