"""Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
 Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в словаре
  для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить."""
import random


def create_word() -> str:
    word = ''.join([chr(random.randint(97, 122)) for _ in range(random.randint(1, 10))])
    return word


def create_dict(list_key, list_value):
    result_dict = {}
    if len(list_key) > len(list_value):
        count = len(list_key) - len(list_value)
        for _ in range(count):
            list_value.append(None)
    elif len(list_key) < len(list_value):
        list_value = list_value[:len(list_key)]
    for i in range(len(list_key)):
        result_dict[list_key[i]] = list_value[i]
    print(result_dict)


if __name__ == '__main__':
    list1 = [create_word() for _ in range(random.randint(1, 10))]
    list2 = [random.randint(1, 100) for _ in range(random.randint(1, 10))]
    create_dict(list1, list2)
