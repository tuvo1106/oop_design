#!/usr/bin/env python3

from abc import ABC, abstractmethod
from cricinfo.data_types.enums import MatchResult


class Match(ABC):
    def __init__(self, number, start_time, referee):
        self.__number = number
        self.__start_time = start_time
        self.__result = MatchResult.LIVE
        self.__teams = []
        self.__innings = []
        self.__umpires = []
        self.__referee = referee
        self.__commentators = []
        self.__match_stats = []

    def assign_stadium(self, stadium):
        pass

    def assign_referee(self, referee):
        pass


class ODI(Match):
    pass


class Test(Match):
    pass
