class MenuItem:
    menu_item_count = 0

    def __init__(self, title, description, price):
        MenuItem.menu_item_count += 1
        self.__menu_item_id = MenuItem.menu_item_count
        self.__title = title
        self.__description = description
        self.__price = price

    def __str__(self):
        return f"id - {self.__menu_item_id}, title - {self.__title},\
description - {self.__description}, price - {self.__price}\n"

    def update_price(self, price):
        self.price = price

    @property
    def menu_item_id(self):
        return self.__menu_item_id

    @menu_item_id.setter
    def menu_item_id(self,menu_item_id):
        self.__menu_item_id = menu_item_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
