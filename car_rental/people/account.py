#!/usr/bin/env python3

from abc import ABC
from car_rental.data_types.enums import AccountStatus


class Account(ABC):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__status = AccountStatus.ACTIVE
        self.__person = person

    def reset_password(self):
        pass


class Member(Account):
    def __init__(self):
        self.__total_vehicles_reserved = 0

    def get_reservations(self):
        pass


class Receptionist(Account):
    def __init__(self, date_joined):
        self.__date_joined = date_joined

    def search_member(self, name):
        pass


class AdditionalDriver:
    def __init__(self, id, person):
        self.__driver_id = id
        self.__person = person
