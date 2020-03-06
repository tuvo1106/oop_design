#!/usr/bin/env python3

from abc import ABC
import datetime
from restaurant.people.person import Person


class Employee(ABC, Person):
    def __init__(self, id, account, name, email, phone):
        super().__init__(name, email, phone)
        self.__employee_id = id
        self.__date_joined = datetime.date.today()
        self.__account = account


class Receptionist(Employee):
    def __init__(self, id, account, name, email, phone):
        super().__init__(id, account, name, email, phone)

    def create_reservation(self):
        pass

    def search_customer(self, name):
        pass


class Manager(Employee):
    def __init__(self, id, account, name, email, phone):
        super().__init__(id, account, name, email, phone)

    def add_employee(self):
        pass


class Chef(Employee):
    def __init__(self, id, account, name, email, phone):
        super().__init__(id, account, name, email, phone)

    def take_order(self):
        None
