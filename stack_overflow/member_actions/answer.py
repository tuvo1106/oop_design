#!/usr/bin/env python3

import datetime


class Answer:
    def __init__(self, text, member):
        self.__answer_text = text
        self.__accepted = False
        self.__vote_count = 0
        self.__flag_count = 0
        self.__creation_time = datetime.datetime.now()
        self.__creating_member = member
        self.__photos = []

    def increment_vote_count(self):
        pass
