#!/usr/bin/env python3

from abc import ABC
import datetime
from linkedin.profile.profile import Profile


class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account


class Member(Person):
    def __init__(self):
        self.__date_of_membership = datetime.date.today()
        self.__headline = ""
        self.__photo = []
        self.__member_suggestions = []
        self.__member_follows = []
        self.__member_connections = []
        self.__company_follows = []
        self.__group_follows = []
        self.__profile = Profile(None, None, None, None, None, None)

    def send_message(self, message):
        pass

    def create_post(self, post):
        pass

    def send_connection_invitation(self, connection_invitation):
        pass


class Admin(Person):
    def block_user(self, customer):
        None

    def unblock_user(self, customer):
        None
