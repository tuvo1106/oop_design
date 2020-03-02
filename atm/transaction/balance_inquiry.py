#!/usr/bin/env python3

from atm.transaction.transaction import Transaction


class BalanceInquiry(Transaction):
    def __init__(self, account_id):
        self.__account_id = account_id

    def get_account_id(self):
        return self.__account_id
