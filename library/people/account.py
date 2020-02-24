#!/usr/bin/env python3

from abc import ABC, abstractmethod
from library.data_types.enums import AccountStatus


class Account(ABC):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__status = status
        self.__person = person

    def reset_password(self):
        pass
