#!/usr/bin/env python3

from parking_lot.people.account import Account


class Admin(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.Active):
        super().__init__(user_name, password, person, status)

    def add_parking_floor(self, floor):
        pass

    def add_parking_spot(self, floor_name, spot):
        pass

    def add_parking_display_board(self, floor_name, display_board):
        pass

    def add_customer_info_panel(self, floor_name, info_panel):
        pass

    def add_entrance_panel(self, entrance_panel):
        pass

    def add_exit_panel(self, exit_panel):
        pass
