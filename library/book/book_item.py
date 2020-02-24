#!/usr/bin/env python3

from library.book.book import Book
from library.book_actions.book_lending import BookLending
from library.data_types.enums import BookStatus


class BookItem(Book):
    def check_for_fine(self, barcode, is_reference_only, borrowed, due_date, price, book_format, status, date_of_purchase, publication_date, placed_at):
        self.__barcode = barcode
        self.__is_reference_only = is_reference_only
        self.__borrowed = borrowed
        self.__due_date = due_date
        self.__price = price
        self.__format = book_format
        self.__status = status
        self.__date_of_purchase = date_of_purchase
        self.__publication_date = publication_date
        self.__placed_at = placed_at

    def update_book_item_status(self, book_status):
        pass

    def checkout(self, member_id):
        if self.get_is_reference_only():
            print("self book is Reference only and can't be issued")
            return False
        if not BookLending.lend_book(self.get_bar_code(), member_id):
            return False
        self.update_book_item_status(BookStatus.LOANED)
        return True

    def get_is_reference_only(self):
        pass

    def get_bar_code(self):
        pass
