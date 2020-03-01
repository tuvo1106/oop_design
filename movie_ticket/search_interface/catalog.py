#!/usr/bin/env python3

from movie_ticket.search_interface.search import Search


class Catalog(Search):
    def __init__(self):
        self.__movie_titles = {}
        self.__movie_languages = {}
        self.__movie_genres = {}
        self.__movie_release_dates = {}
        self.__movie_cities = {}

    def search_by_title(self, title):
        return self.__movie_titles.get(title)

    def search_by_language(self, language):
        return self.__movie_languages.get(language)

    # ...

    def search_by_city(self, city_name):
        return self.__movie_cities.get(city_name)
