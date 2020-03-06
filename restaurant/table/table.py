#!/usr/bin/env python3

from restaurant.data_types.enums import TableStatus


class Table:
    def __init__(self, id, max_capacity, location_identifier,
                 status=TableStatus.FREE):
        self.__table_id = id
        self.__max_capacity = max_capacity
        self.__location_identifier = location_identifier
        self.__status = status
        self.__seats = []

    def is_table_free(self):
        pass

    def add_reservation(self):
        pass

    def search(self, capacity, start_time):
        # return all tables with the given capacity and availability
        pass
