"""Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль необходимо
 исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
 “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря."""
import time


def gen(start: int, finish: int):
    rand_list: list = []
    rand_dict: dict = {}

    if start > finish:
        start, finish = finish, start

    if start == 0:
        start = 1
    elif finish == 0:
        finish = -1

    for i in range(10):
        random = int(time.time() * 100000)
        random %= finish - start
        random += start
        time.sleep(abs(random) / 1000)
        rand_list.append(random)
        rand_dict[f'elem_{i}'] = random
    return rand_list, rand_dict


def main():
    print(gen(0, 50))


if __name__ == '__main__':
    main()
