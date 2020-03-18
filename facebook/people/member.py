#!/usr/bin/env python3

from facebook.people.person import Person
from facebook.profile.profile import Profile


class Member(Person):
    def __init__(self, id, date_of_membership, name):
        self.__member_id = id
        self.__date_of_membership = date_of_membership
        self.__name = name
        self.__profile = Profile(None, None, None)
        self.__member_follows = []
        self.__member_connections = []
        self.__page_follows = []
        self.__member_suggestions = []
        self.__connection_invitations = []
        self.__group_follows = []

    def send_message(self, message):
        pass

    def create_post(self, post):
        pass

    def send_connection_invitation(self, invitation):
        pass

    def search_member_suggestions(self):
        pass
