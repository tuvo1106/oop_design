#!/usr/bin/env python3

from library.people.account import Account
from library.data_types.enums import AccountStatus


class Librarian(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id, password, person, status)

    def add_book_item(self, book_item):
        pass

    def block_member(self, member):
        pass

    def un_block_member(self, member):
        pass
