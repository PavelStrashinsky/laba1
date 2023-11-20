import random
a = [random.randint(-100, 100) for i in range(10)]
b = tuple(a)
print(b)
ans = 0
for i in range(10):
     if b[i] > 0:
         ans = ans + 1
print("Количество положительных элементов: ", ans)