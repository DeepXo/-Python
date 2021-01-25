print("Введите секунды!")
sec = int(input())
hours = sec//3600
minutes = hours//60
if hours<1:
    print(f"Данное колличество секунд составляет {minutes} минут ")
elif hours>=1:
    print(f"Данное колличество секунд составляет {hours} часов и {minutes} минут")
