"====Переменные===="
# переменные - это ссылки на ячейки памяти, где хранятся какие-то данные
a = 4

"====Ввод и вывод данных===="
a = input()
print(a)
# print - функция ввода данных в терминал
# input - функция вывода данных с терминала
a = input()
print("Введенное число", a)

"====Числа===="
# integers(int) - целы числа (-5, 0, 7)
# float - вещественные (с плавающей точной) (0.3, 0.345, -345.563)
# decimal - точное вещественное число
# чтобы использовать decimal нужно его импортировать
from decimal import Decimal
c = Decimal(0.1)

# complex - комплексные числа
complex(1, 5)

"====Операции над числами===="
5 + 5 #сложение
10 - 3 #вычитание
2 * 3 #умножение
15 / 3 #деление (float 5.0)
15 // 2 #целочисленное деление (int 7)
5 % 2 #остаток от деления (int 1)
5 ** 2 #возведение в степень
25 ** 0.5 #квадратный корень числа

# модуль числа - абсолютное значение числа
abs (-5) # 5
pow (2,3) # 2**3 = 8
pow (2,3,4) # возвращает остаток от деления результата умножения на третье число
# (2 ** 3) % 4 = 0

#divmod - функция, которая принимает 2 числа и возвращает 2 числа, где 
#первое - это целая часть от деления, а второе - остаток от деления
divmod(15, 2) # 7,1
divmod(9, 3) # 3,0

# round - функция, которая округляет число
round (5.6) # 6
round (3.5) # 4
round (7.49) # 7 (берет первую цифру после точки)
# можно указать сколько цифр после запятой оставить
round (10.0475, 3) # 10.048
round (10.0474, 3) # 10.047
# sqrt - функция для нахождения корня числа
# для работы нужно её импортировать из библиотеки math
from math import sqrt
sqrt(36) # 6
8 ** (1/3) # 2
# функция int - меняет тип данных на integer

