#!/usr/bin/env python3

from abc import ABC
import datetime
from brokerage.data_types.enums import TimeEnforcementType, OrderStatus


class Order(ABC):
    def __init__(self, id):
        self.__order_id = id
        self.__is_buy_order = False
        self.__status = OrderStatus.OPEN
        self.__time_enforcement = TimeEnforcementType.ON_THE_OPEN
        self.__creation_time = datetime.datetime.now()
        self.__parts = {}

    def set_status(self, status):
        self.status = status

    def save_in_DB(self):
        # save in the database
        pass

    def add_order_parts(self, parts):
        for part in parts:
            self.__parts[part.get_id()] = part

    def get_order_id(self):
        pass


class LimitOrder(Order):
    def __init__(self):
        self.__price_limit = 0.0
