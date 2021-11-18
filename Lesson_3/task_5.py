"""Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
 заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
  (функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
   вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод
    всех подстрок, состоящих из букв и цифр, например: example345."""

# Не понял, что означает "Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод
# первого вхождения, вывод всех вхождений." Пропустил...
from random import randint
from pathlib import Path


def create_word() -> str:
    word = ''.join([chr(randint(97, 122)) for _ in range(randint(1, 10))])
    return word


def create_num() -> int:
    num = randint(1, 100)
    return num


def create_file():
    file = Path('file.txt')
    if file.exists():
        print('Такой файл уже существует')
    else:
        with open(file, 'w', encoding='utf-8') as f:
            list_word = [create_word() for _ in range(10)]
            list_num = [create_num() if randint(0, 1) else f'{create_word()}{create_num()}' for _ in range(10)]
            list_result = [f'{i} {j}\n' for i, j in zip(list_word, list_num)]
            f.writelines(list_result)
    print_file(file)


def print_file(file):
    # Создаем пустой список. Сюда будем складывать строки из файла
    list_line = []
    with open(file, 'r') as f:
        for line in f.readlines():
            # Здесь отсекаем у строки перевод коретки и добавляем её в список
            list_line.append(line[:-1])
    for line in list_line:
        # Проверяем является ли вторая часть строки числом
        if line.split()[1].isdigit():
            continue
        # ...и если нет, то печатаем её
        print(line)


if __name__ == '__main__':
    create_file()
