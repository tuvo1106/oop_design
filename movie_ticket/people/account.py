#!/usr/bin/env python3

from movie_ticket.data_types.enums import AccountStatus


class Account:
    def __init__(self, id, password, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__status = status

    def reset_password(self):
        pass
