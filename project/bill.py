class Bill:
    bill_count = 0

    def __init__(self, payment_type):
        Bill.bill_count += 1
        self.__bill_id = Bill.bill_count
        self.__payment_type = payment_type
        self.__payment_status = False

    def __str__(self):
        return f"id - {self.__bill_id}, payment type - {self.__payment_type},\
    payment status - {self.__payment_status}.\n"

    def pay(self):
        self.payment_status = True

    def change_type(self, payment_type):
        if not self.__payment_status:
            self.payment_type = payment_type


    @property
    def bill_id(self):
        return self.__bill_id

    @bill_id.setter
    def bill_id(self, bill_id):
        self.__bill_id = bill_id

    @property
    def payment_type(self):
        return self.__payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        self.__payment_type = payment_type

    @property
    def payment_status(self):
        return self.__payment_status

    @payment_status.setter
    def payment_status(self, status):
        self.__payment_status = status
