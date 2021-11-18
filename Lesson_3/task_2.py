"""Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением, целое
 оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они совпадают,
  программа должна возвращать значение True, иначе False."""
from decimal import Decimal
from math import modf


def check_num():
    num = float(input('Введите число: '))
    float_num, int_num = modf(num)
    float_num = Decimal(str(float_num))
    float_num = float_num.quantize(Decimal(str(num)))
    if float_num == 0:
        print('Число целое')
    else:
        int_num = int(int_num)
        float_num = int(float_num * (int(f'1{"".join(["0" for _ in range(len(str(float_num)) - 2)])}')))
        if int_num == float_num:
            print(True)
        else:
            print(False)


if __name__ == '__main__':
    check_num()
