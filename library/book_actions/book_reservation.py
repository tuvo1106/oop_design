#!/usr/bin/env python3


class BookReservation:
    def check_for_fine(self, creation_date, status, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__status = status
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    @classmethod
    def fetch_reservation_details(self, barcode):
        pass
