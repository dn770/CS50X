from order import Order


class Shipping:

    shipping_count = 0

    def __init__(self, shipping_address):
        Shipping.shipping_count += 1
        self.__shipping_id = Shipping.shipping_count
        self.__shipping_address = shipping_address
        self.__order_id = 0

    def change_address(self, shipping_address):
        self.shipping_address = shipping_address


    @property
    def shipping_id(self):
        return self.__shipping_id

    @shipping_id.setter
    def shipping_id(self, shipping_id):
        self.__shipping_id = shipping_id

    @property
    def shipping_address(self):
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        self.__shipping_address = shipping_address

    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def order_id(self, order_id):
        self.__order_id = order_id
