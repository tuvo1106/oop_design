#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Search(ABC):
    def search_products_by_name(self, name):
        pass

    def search_products_by_category(self, category):
        pass
