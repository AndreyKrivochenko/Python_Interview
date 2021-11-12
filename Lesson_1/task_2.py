"""Дополнить следующую функцию недостающим кодом:"""
import os


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    print(sPath)
    for directory in os.listdir(sPath):
        path = os.path.join(sPath, directory)
        print(' ' + path)
        if os.path.isdir(path):
            print('dir')
            print_directory_contents(path)


def main():
    print_directory_contents(os.getcwd())


if __name__ == '__main__':
    main()
