#!/usr/bin/env python3

from atm.transaction.transaction import Transaction


class Withdraw(Transaction):
    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount
