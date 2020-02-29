#!/usr/bin/env python3


class Tag:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__daily_asked_frequency = 0
        self.__weekly_asked_frequency = 0
