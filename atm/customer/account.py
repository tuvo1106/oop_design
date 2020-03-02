#!/usr/bin/env python3


class Account:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__total_balance = 0.0
        self.__available_balance = 0.0

    def get_available_balance(self):
        return self.__available_balance


class SavingAccount(Account):
    def __init__(self, withdraw_limit):
        self.__withdraw_limit = withdraw_limit


class CheckingAccount(Account):
    def __init__(self, debit_card_number):
        self.__debit_card_number = debit_card_number
