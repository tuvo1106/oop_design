#!/usr/bin/env python3

from parking_lot.data_types.enums import AccountStatus


class Account:
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        self.__user_name = user_name
        self.__password = password
        self.__person = person
        self.__status = status

    def reset_password(self):
        pass
