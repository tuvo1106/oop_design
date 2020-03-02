#!/usr/bin/env python3

from atm.components.cash_dispenser import CashDispenser
from atm.components.keypad import Keypad
from atm.components.screen import Screen
from atm.components.printer import Printer
from atm.components.deposit_slot import CheckDepositSlot, CashDepositSlot


class ATM:
    def __init__(self, id, location):
        self.__atm_id = id
        self.__location = location
        self.__cash_dispenser = CashDispenser()
        self.__keypad = Keypad()
        self.__screen = Screen()
        self.__printer = Printer()
        self.__check_deposit = CheckDepositSlot()
        self.__cash_deposit = CashDepositSlot()

    def authenticate_user(self):
        pass

    def make_transaction(self, customer, transaction):
        pass
