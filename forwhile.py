for i in range(1, 11):
    print(i)

N = int(input("Введите число N: "))
for i in range(1, N + 1):
    print(i)

i = 1
sum = 0

while i <= 100:
    sum += i
    i += 1

print("Сумма всех чисел от 1 до 100:", sum)
