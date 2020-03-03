#!/usr/bin/env python3


class Flight:
    def __init__(self, flight_number, departure, arrival, duration_in_minutes):
        self.__flight_number = flight_number
        self.__departure = departure
        self.__arrival = arrival
        self.__duration_in_minutes = duration_in_minutes
        self.__weekly_schedules = []
        self.__custom_schedules = []
        self.__flight_instances = []
