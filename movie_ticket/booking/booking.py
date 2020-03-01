#!/usr/bin/env python3

import datetime


class Booking:
    def __init__(self, booking_number, number_of_seats, status, show,
                 show_seats, payment):
        self.__booking_number = booking_number
        self.__number_of_seats = number_of_seats
        self.__created_on = datetime.date.today()
        self.__status = status
        self.__show = show
        self.__seats = show_seats
        self.__payment = payment

    def make_payment(self, payment):
        pass

    def cancel(self):
        pass

    def assign_seats(self, seats):
        pass
