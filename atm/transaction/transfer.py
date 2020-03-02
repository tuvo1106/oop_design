#!/usr/bin/env python3

from atm.transaction.transaction import Transaction


class Transfer(Transaction):
    def __init__(self, destination_account_number):
        self.__destination_account_number = destination_account_number

    def get_destination_account(self):
        return self.__destination_account_number
