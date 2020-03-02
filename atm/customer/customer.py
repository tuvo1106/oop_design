#!/usr/bin/env python3

from atm.customer.account import Account


class Customer:
    def __init__(self, name, address, email, phone, status):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = status
        self.__card = Card()
        self.__account = Account

    def make_transaction(self, transaction):
        pass

    def get_billing_address(self):
        pass
