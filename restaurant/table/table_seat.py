#!/usr/bin/env python3

from restaurant.data_types.enums import SeatType


class TableSeat:
    def __init__(self):
        self.__table_seat_number = 0
        self.__type = SeatType.REGULAR

    def update_seat_type(self, seat_type):
        pass
