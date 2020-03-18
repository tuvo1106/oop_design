#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Search(ABC):
    def search_member(self, name):
        pass

    def search_group(self, name):
        pass

    def search_page(self, name):
        pass

    def search_post(self, word):
        pass


class SearchIndex(Search):
    def __init__(self):
        self.__member_names = {}
        self.__group_names = {}
        self.__page_titles = {}
        self.__posts = {}

    def add_member(self, member):
        if member.get_name() in self.__member_names:
            self.__member_names.get(member.get_name()).add(member)
        else:
            self.__member_names[member.get_name()] = member

    def add_group(self, group):
        pass

    def add_page(self, page):
        pass

    def add_post(self, post):
        pass

    def search_member(self, name):
        return self.__member_names.get(name)

    def search_group(self, name):
        return self.__group_names.get(name)

    def search_page(self, name):
        return self.__page_titles.get(name)

    def search_post(self, word):
        return self.__posts.get(word)
