from customer import Customer
from bill import Bill


class Order:
    order_id = 0

    def __init__(self, table_id, customer_id, payment_type):
        Order.order_id += 1
        self.__order_id = Order.order_id
        self.__order_status = False
        self.__order_price = 0
        self.__table_id = table_id
        self.__customer_id = customer_id
        self.__bill = Bill(payment_type)
        self.__order_items = []

    def __str__(self):
        rstr = f"id - {self.__order_id}, status - {self.__order_status},\
price - {self.__order_price}, table id - {self.__table_id},  customer id - {self.__customer_id}.\
items: \n"
        for item in self.__order_items:
            rstr = rstr + " " + str(item.menu_item_id)+ " " + item.description + " " + str(item.price) + "\n"
        rstr = rstr + "bill- " + str(self.bill.bill_id) + " " + str(self.bill.payment_type) + " " + str(self.bill.payment_status) + "\n"
        return rstr

    def calculate_price(self):
        p_sum = 0
        for item in self.__order_items:
            p_sum += item.price
        self.__order_price = p_sum
        return p_sum


    def remove_menu_item(self, menu_item_id):
        for item in self.__order_items:
            if item.menu_item_id == menu_item_id:
                self.__order_items.remove(item)
                break
        self.calculate_price()


    @property
    def orderID(self):
        return self.__orderID

    @orderID.setter
    def orderID(self, orderID):
        self.__orderID = orderID

    @property
    def order_status(self):
        return self.__order_status

    @order_status.setter
    def order_status(self, order_status):
        self.__order_status = order_status
    @property
    def order_items(self):
        return self.__order_items

    @order_items.setter
    def order_items(self, order_items):
        self.__order_items = order_items

    @property
    def order_price(self):
        return self.__order_price

    @order_price.setter
    def order_price(self, order_price):
        self.__order_price = order_price

    @property
    def table_id(self):
        return self.__table_id

    @table_id.setter
    def table(self, table_id):
        self.__table_id = table_id

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self.__customer_id = customer_id

    @property
    def bill(self):
        return self.__bill

    @bill.setter
    def bill(self, bill):
        self.__bill = bill
