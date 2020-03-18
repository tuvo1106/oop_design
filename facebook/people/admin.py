#!/usr/bin/env python3

from facebook.people.person import Person


class Admin(Person):
    def block_user(self, customer):
        pass

    def unblock_user(self, customer):
        pass

    def enable_page(self, page):
        pass

    def disable_page(self, page):
        pass
