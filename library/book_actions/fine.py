#!/usr/bin/env python3


class Fine:
    def check_for_fine(self, creation_date, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    @classmethod
    def collect_fine(self, member_id, days):
        pass
