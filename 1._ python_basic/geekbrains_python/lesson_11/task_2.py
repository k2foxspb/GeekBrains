

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_1 = int(input("введите число: "))
num_2 = int(input("введите число: "))
try:
    if num_2 == 0:
        raise OwnError("Вы ввели отрицательное число!")
    x = num_1 / num_2
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {x}")

