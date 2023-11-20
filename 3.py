import random
sum1 = 0
sum2 = 0
c0 = 0
list = [random.randint(-100,100) for i in range(10)]
print(list)
for i in range(10):
    if list[i] > 0:
        sum1 = sum1 + list[i]
    if (list[i] == 0) and (c0 == 0):
        for j in range(i + 1, 10):
            sum2 = sum2 + list[j]
            c0 = c0 + 1
i = 0
while i < len(list):
    if (list[i] < 0):
        list.pop(i)
    else: i = i + 1
print("Сумма положительных элементов: ", sum1)
if c0 == 0:
    print("Сумму посчитать нельзя")
else: print("Сумма элементов списка после первого нуля: ", sum2)
print(list)