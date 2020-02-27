#!/usr/bin/env python3

from online_shopping.search_interface.search import Search


class Catalog(Search):
    def __init__(self):
        self.__product_names = {}
        self.__product_categories = {}

    def search_products_by_name(self, name):
        return self.__product_names.get(name)

    def search_products_by_category(self, category):
        return self.__product_categories.get(category)
