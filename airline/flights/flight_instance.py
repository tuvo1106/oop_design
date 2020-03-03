#!/usr/bin/env python3


class FlightInstance:
    def __init__(self, departure_time, gate, status, aircraft):
        self.__departure_time = departure_time
        self.__gate = gate
        self.__status = status
        self.__aircraft = aircraft

    def cancel(self):
        pass

    def update_status(self, status):
        pass
