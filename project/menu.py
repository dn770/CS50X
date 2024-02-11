from menuItem import MenuItem


class Menu:
    menu_count = 0

    def __init__(self, menu_type):
        Menu.menu_count += 1
        self.__menu_id = Menu.menu_count
        self.__menu_type = menu_type
        self.__items = []

    def __str__(self):
        rstr = f"id - {self.__menu_id}, type - {self.__menu_type},items:\n"
        for item in self.__items:
            rstr = rstr + " " + str(item.menu_item_id)+ " " + item.description + " " + str(item.price) + "\n"
        return rstr

    def add_menu_item(self, title, description, price):
        item = MenuItem(title, description, price)
        self.__items.append(item)

    def remove_menu_item(self, menu_item_id):
        for item in self.__items:
            if item.menu_item_id == menu_item_id:
                self.__items.remove(item)
                break

    def clear_menu(self):
        self.__items.clear()

    @property
    def menu_id(self):
        return self.__menu_id

    @menu_id.setter
    def menu_id(self, menu_id):
        self.__menu_id = menu_id

    @property
    def menu_type(self):
        return self.__menu_type

    @menu_type.setter
    def menu_type(self, menu_type):
        self.__menu_type = menu_type

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        self.__items = items
