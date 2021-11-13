class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{self._ItemDiscount__name} - {self._ItemDiscount__price}')


item = ItemDiscountReport(name='Item_1', price=34)
item.get_parent_data()
