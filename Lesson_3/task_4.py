"""Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл. Если файл
 с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить два списка:
  с текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам функцию zip().
   Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом, чтобы каждая строка
    файла содержала текстовое и числовое значение. Вызвать вторую функцию. В нее должна передаваться ссылка на созданный
     файл. Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого. Вся программа
      должна запускаться по вызову первой функции."""
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
            list_num = [create_num() for _ in range(10)]
            list_result = [f'{i}\t{j}\n' for i, j in zip(list_word, list_num)]
            f.writelines(list_result)
    print_file(file)


def print_file(file):
    with open(file, 'r') as f:
        print(f.read())


if __name__ == '__main__':
    create_file()
