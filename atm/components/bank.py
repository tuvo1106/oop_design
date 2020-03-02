#!/usr/bin/env python3


class Bank:
    def __init__(self, name, bank_code):
        self.__name = name
        self.__bank_code = bank_code

    def get_bank_code(self):
        return self.__bank_code

    def add_atm(self, atm):
        pass
