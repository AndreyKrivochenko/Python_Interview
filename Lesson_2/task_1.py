class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{self.name} - {self.price}')


item = ItemDiscountReport(name='Item_1', price=34)
item.get_parent_data()
