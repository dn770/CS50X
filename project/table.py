from order import Order


class Table:
    table_count = 0

    def __init__(self, max_capacity):
        Table.table_count += 1
        self.__table_id = Table.table_count
        self.__table_status = False
        self.__max_capacity = max_capacity
        self.__reservation_id = 0

    def __str__(self):
        return f"id - {self.__table_id}, status - {self.__table_status},\
max capacity - {self.__max_capacity}, reservation_id - {self.__reservation_id}.\n"

    def free_table(self):
        self.__table_status = False

    @property
    def table_id(self):
        return self.__table_id

    @table_id.setter
    def table_id(self, table_id):
        self.__table_id = table_id

    @property
    def table_status(self):
        return self.__table_status

    @table_status.setter
    def table_status(self, table_status):
        self.__table_status = table_status

    @property
    def max_capacity(self):
        return self.__max_capacity

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        self.__max_capacity = max_capacity

    @property
    def reservation_id(self):
        return self.__reservation_id

    @reservation_id.setter
    def reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id
