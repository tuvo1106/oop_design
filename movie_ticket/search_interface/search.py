#!/usr/bin/env python3


from abc import ABC, abstractmethod


class Search(ABC):
    def search_by_title(self, title):
        pass

    def search_by_language(self, language):
        pass

    def search_by_genre(self, genre):
        pass

    def search_by_release_date(self, rel_date):
        pass

    def search_by_city(self, city_name):
        pass
