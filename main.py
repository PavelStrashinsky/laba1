n = int(input("Введите натуральное число: "))
i = 0
while n > 0:
    n1 = n % 10
    n = n // 10
    n2 = n % 10
    if n1 < n2:
        i = 1
if i == 1:
    print("Не является")
else:
    print("Является")
