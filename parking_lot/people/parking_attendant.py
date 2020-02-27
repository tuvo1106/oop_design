#!/usr/bin/env python3

from parking_lot.people.account import Account


class ParkingAttendant(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.Active):
        super().__init__(user_name, password, person, status)

    def process_ticket(self, ticket_number):
        pass
