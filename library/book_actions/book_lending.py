#!/usr/bin/env python3


class BookLending:
    def check_for_fine(self, creation_date, due_date, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__due_date = due_date
        self.__return_date = None
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    @classmethod
    def lend_book(self, barcode, member_id):
        pass

    @classmethod
    def fetch_lending_details(self, barcode):
        pass

    def get_due_date(self):
        pass
