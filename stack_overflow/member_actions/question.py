#!/usr/bin/env python3

import datetime
from abc import ABC, abstractmethod
from stack_overflow.data_types.enums import QuestionStatus, QuestionClosingRemark


class Search(ABC):
    def search(self, query):
        pass


class Question(Search):
    def __init__(self, title, description, bounty, asking_member):
        self.__title = title
        self.__description = description
        self.__view_count = 0
        self.__vote_count = 0
        self.__creation_time = datetime.datetime.now()
        self.__update_time = datetime.datetime.now()
        self.__status = QuestionStatus.OPEN
        self.__closing_remark = QuestionClosingRemark.DUPLICATE
        self.__bounty = bounty
        self.__asking_member = asking_member
        self.__photos = []
        self.__comments = []
        self.__answers = []

    def close(self):
        pass

    def undelete(self):
        pass

    def add_comment(self, comment):
        pass

    def add_bounty(self, bounty):
        pass

    def search(self, query):
        # return all questions containing the string query in their title or
        # description.
        pass
