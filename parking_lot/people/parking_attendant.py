#!/usr/bin/env python3

from parking_lot.data_types.enums import AccountStatus
from parking_lot.people.account import Account


class ParkingAttendant(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        super().__init__(user_name, password, person, status)

    def process_ticket(self, ticket_number):
        pass
