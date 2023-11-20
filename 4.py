s = str(input("Введите последовательность: "))
d = {}
for i in range(len(s)):
    d[int(s[i])] = len(s)
print(d)