#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Transaction(ABC):
    def __init__(self, id, creation_date, status):
        self.__transaction_id = id
        self.__creation_time = creation_date
        self.__status = status

    def make_transation(self):
        pass
