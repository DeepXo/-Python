print("Введите положительное число!")
a = int(input())
max_ch = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > max_ch:
        max_ch = a % 10
    if a > 9:
        continue
    else:
        print(f'Максимальная цифра в числе {max_ch}')
        break