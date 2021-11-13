class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_price(self, val):
        self.__price = val


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount=None):
        self.discount = discount
        super().__init__(name, price)

    def get_parent_data(self):
        print(f'{self._ItemDiscount__name} - {self._ItemDiscount__price}')

    def __str__(self):
        return f'{self._ItemDiscount__name} - цена со скидкой' \
               f' {self._ItemDiscount__price - self._ItemDiscount__price * self.discount / 100} '


item = ItemDiscountReport(name='Item_1', price=34, discount=5)
item.get_parent_data()
item.set_price(45)
item.get_parent_data()
print(item)
