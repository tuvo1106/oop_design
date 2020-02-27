#!/usr/bin/env python3

from online_shopping.data_types.enums import AccountStatus


class Account:
    def __init__(self, user_name, password, name, email, phone, shipping_address,
                 status=AccountStatus):
        self.__user_name = user_name
        self.__password = password
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__shipping_address = shipping_address
        self.__status = status.ACTIVE
        self.__credit_cards = []
        self.__bank_accounts = []

    def add_product(self, product):
        pass

    def add_productReview(self, review):
        pass

    def reset_password(self):
        pass
