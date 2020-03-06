#!/usr/bin/env python3

from abc import ABC


class Person(ABC):
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone
