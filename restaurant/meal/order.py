#!/usr/bin/env python3

import datetime


class Check:
    pass


class Order:
    def __init__(self, id, status, table, waiter, chef):
        self.__order_id = id
        self.__OrderStatus = status
        self.__creation_time = datetime.datetime.now()
        self.__meals = []
        self.__table = table
        self.__waiter = waiter
        self.__chef = chef
        self.__check = Check()

    def add_meal(self, meal):
        pass

    def remove_meal(self, meal):
        pass

    def get_status(self):
        return self.__OrderStatus

    def set_status(self, status):
        pass
