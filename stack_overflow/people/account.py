#!/usr/bin/env python3

from stack_overflow.data_types.enums import AccountStatus


class Account:
    def __init__(self, id, password, name, address, email, phone,
                 status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = status
        self.__reputation = 0

    def reset_password(self):
        pass
