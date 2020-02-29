#!/usr/bin/env python3

import datetime


class Comment:
    def __init__(self, text, member):
        self.__text = text
        self.__creation_time = datetime.datetime.now()
        self.__flag_count = 0
        self.__vote_count = 0
        self.__asking_member = member

    def increment_vote_count(self):
        pass
