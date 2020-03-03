#!/usr/bin/env python3

from airline.airport.seat import Seat


class FlightSeat(Seat):
    def __init__(self, fare):
        self.__fare = fare

    def get_fare(self):
        return self.__fare
