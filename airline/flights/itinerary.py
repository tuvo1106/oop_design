#!/usr/bin/env python3


class Itinerary:
    def __init__(self, customer_id, starting_airport, final_airport,
                 creation_date):
        self.__customer_id = customer_id
        self.__starting_airport = starting_airport
        self.__final_airport = final_airport
        self.__creation_date = creation_date
        self.__reservations = []

    def get_reservations(self):
        pass

    def make_reservation(self):
        pass

    def make_payment(self):
        pass
