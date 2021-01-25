print("Введите число больше 0 и меньше 10!")
a = int(input())
res = (a+int(str(a)+str(a))+int(str(a)+str(a)+str(a)))
if 0 < a < 10:
    print(f"Результат примера {res}")
    print("Спасибо за участие!")
elif a <= 0 or a >= 10:
    print("Введите корректные значения")