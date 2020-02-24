#!/usr/bin/env python3

from abc import ABC


class Search(ABC):
    def search_by_title(self, title):
        pass

    def search_by_author(self, author):
        pass

    def search_by_subject(self, subject):
        pass

    def search_by_pub_date(self, publish_date):
        pass
