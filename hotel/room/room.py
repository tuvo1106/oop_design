#!/usr/bin/env python3

from abc import ABC


class Search(ABC):
    def search(self, style, start_date, duration):
        None


class Room(Search):
    def __init__(self, room_number, room_style, status, price, is_smoking):
        self.__room_number = room_number
        self.__style = room_style
        self.__status = status
        self.__booking_price = price
        self.__is_smoking = is_smoking
        self.__keys = []
        self.__house_keeping_log = []

    def is_room_available(self):
        pass

    def check_in(self):
        pass

    def check_out(self):
        pass

    def search(self, style, start_date, duration):
        # return all rooms with the given style and availability
        pass
