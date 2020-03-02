#!/usr/bin/env python3

from abc import ABC, abstractmethod


class DepositSlot(ABC):
    def __init__(self):
        self.__total_amount = 0.0

    def get_total_amount(self):
        return self.__total_amount


class CheckDepositSlot(DepositSlot):
    def get_check_amount(self):
        pass


class CashDepositSlot(DepositSlot):
    def receive_dollar_bill(self):
        pass
