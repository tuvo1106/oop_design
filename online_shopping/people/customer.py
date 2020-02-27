#!/usr/bin/env python3

from abc import ABC


class Customer(ABC):
    def __init__(self, cart, order):
        self.__cart = cart
        self.__order = order

    def get_shopping_cart(self):
        return self.__cart

    def add_item_to_cart(self, item):
        pass

    def remove_item_from_cart(self, item):
        pass


class Guest(Customer):
    def register_account(self):
        pass


class Member(Customer):
    def __init__(self, account):
        self.__account = account

    def place_order(self, order):
        pass
