#!/usr/bin/env python3

from enum import Enum


class BookFormat(Enum):
    HARDCOVER = 1,
    PAPERBACK = 2,
    AUDIO_BOOK = 3,
    EBOOK = 4,
    NEWSPAPER = 5,
    MAGAZINE = 6,
    JOURNAL = 7


class BookStatus(Enum):
    AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4


class ReservationStatus(Enum):
    COMPLETED, WAITING, PENDING, CANCELED, NONE = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5
