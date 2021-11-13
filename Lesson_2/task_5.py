class ItemDiscount:
    name = 'Name'
    price = 34


class ItemDiscountReportFirst(ItemDiscount):
    def get_info(self):
        print(self.name)


class ItemDiscountReportSecond(ItemDiscount):
    def get_info(self):
        print(self.price)


def obj_handler(obj):
    obj.get_info()


item_1 = ItemDiscountReportFirst()
item_2 = ItemDiscountReportSecond()

# 1
item_1.get_info()
item_2.get_info()

# 2
for obj in (item_1, item_2):
    obj.get_info()

# 3
obj_handler(item_1)
obj_handler(item_2)
