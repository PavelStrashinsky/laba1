s = str(input("Введите строку: "))
ans1 = 0
ans2 = 0
ans3 = 0
for i in range(len(s) - 1):
    if ((s[i].isupper() and s[i + 1].isupper()) or (s[i].islower() and s[i + 1].islower())):
        ans1 = ans1 + 1

for i in range(len(s)):
    print(s[i])
    if (s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U' or s[i] == 'Y' or s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'y'):
        ans2 = ans2 + 1
print("Количество пар: ", ans1)
print("Количество гласных: ", ans2)
