#!/usr/bin/env python3


class VehicleLog:
    def __init__(self, id, type, description, creation_date):
        self.__id = id
        self.__type = type
        self.__description = description
        self.__creation_date = creation_date

    def update(self):
        pass

    def search_by_log_type(self, type):
        pass
