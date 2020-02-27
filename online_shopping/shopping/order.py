#!/usr/bin/env python3

import datetime
from online_shopping.data_types.enums import OrderStatus


class Order:
    def __init__(self, order_number, status=OrderStatus.PENDING):
        self.__order_number = 0
        self.__status = status
        self.__order_date = datetime.date.today()
        self.__order_log = []

    def send_for_shipment(self):
        pass

    def make_payment(self, payment):
        pass

    def add_order_log(self, order_log):
        pass
