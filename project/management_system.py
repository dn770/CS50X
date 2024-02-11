from restaurant import Restaurant
from menu import Menu
from customer import Customer
from reservation import Reservation
from table import Table
from shipping import Shipping
from order import Order


class ManagementSystem(Restaurant):

    def __init__(self, name , adderss, phone_number ,description):
        super().__init__(name , adderss, phone_number ,description)
        self.__menus = []
        self.__tables = []
        self.__customers = []
        self.__orders = []

    def add_menu(self, type):
        menu = Menu(type)
        self.__menus.append(menu)
        return menu

    def remove_menu(self, menu_id):
        for menu in self.menus:
            if menu.menu_id == menu_id:
                self.menus.remove(menu)
                return True

    def add_table(self,max_capacity):
        table = Table(max_capacity)
        self.__tables.append(table)

    def remove_table(self, table_id):
        for table in self.tables:
            if table.table_id == table_id:
                self.__tables.remove(table)

    def add_customer(self, name, contant_number):
        customer = Customer(name, contant_number)
        self.__customers.append(customer)
        return customer

    def remove_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer.id:
                self.__customers.remove(customer)

    def create_order(self, table_id, customer, payment_type):
        new_order = Order(table_id, customer.customer_id, payment_type)
        self.__orders.append(new_order)
        return new_order

    def take_order(self):
        for order in self.orders:
            if not order.order_status:
                order.status = True
                return order

    def remove_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                if order.table_id:
                    Table.free_table(order.table_id)
                self.__orders.remove(order)
                break

    def create_reservation(self, time, num_of_people):
        reservation = Reservation(time, num_of_people)
        return reservation

    def match_table(self, reservation):
        for table in self.tables:
            if not table.table_status and int(table.max_capacity) // 2 <= int(reservation.number_of_people) <= int(table.max_capacity):
                table.__reservation_id = reservation.reservation_id
                table.__table_status = True
                return table.table_id
        return 0

    def create_shipping(self,address):
        shipping = Shipping(address)
        return shipping

    def update_order(self, order, menu_id, menu_item_id):
        for menu in self.menus:
            if menu.menu_id == menu_id:
                for item in menu:
                    if item.menu_item_id == menu_item_id:
                        order.__order_items.append(item)
                        order.calculate_price()
                        break

    @property
    def menus(self):
        return self.__menus

    @menus.setter
    def menus(self,menus):
        self.__menus = menus

    @property
    def tables(self):
        return self.__tables

    @tables.setter
    def tables(self, tables):
        self.__tables = tables

    @property
    def customers(self):
        return self.__customers

    @customers.setter
    def customers(self, customers):
        self.__customers = customers

    @property
    def orders(self):
        return self.__orders

    @orders.setter
    def orders(self, orders):
        self.__orders = orders

    @property
    def reservations(self):
        return self.__reservations

    @reservations.setter
    def reservations(self, reservations):
        self.__reservations = reservations
