#!/usr/bin/env python3


class Member:
    def __init__(self, account):
        self.__account = account
        self.__badges = []

    def get_reputation(self):
        return self.__account.get_reputation()

    def get_email(self):
        return self.__account.get_email()

    def create_question(self, question):
        pass

    def create_tag(self, tag):
        pass


class Admin(Member):
    def block_member(self, member):
        pass

    def unblock_member(self, member):
        pass


class Moderator(Member):
    def close_question(self, question):
        pass

    def undelete_question(self, question):
        pass
