#!/usr/bin/env python3

import datetime
from abc import ABC, abstractmethod
from brokerage.data_types.enums import AccountStatus


class Account(ABC):
    def __init__(self, id, password, name, address, email, phone, status=AccountStatus.NONE):
        self.__id = id
        self.__password = password
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = AccountStatus.NONE

    def reset_password(self):
        pass
