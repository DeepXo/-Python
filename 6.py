print("Введите начальный результат")
a = int(input())
print("Введите желаемый результат")
b = int(input())
days = 1
res_km = a
while res_km < b:
    a = a+0.1*a
    days += 1
    res_km = a
print(f'Желаемый результат будет достигнут на {days} день!')
