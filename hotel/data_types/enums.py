#!/usr/bin/env python3

from enum import Enum


class RoomStyle(Enum):
    STANDARD, DELUXE, FAMILY_SUITE, BUSINESS_SUITE = 1, 2, 3, 4


class RoomStatus(Enum):
    AVAILABLE = 1
    RESERVED = 2
    OCCUPIED = 3
    NOT_AVAILABLE = 4
    BEING_SERVICED = 5
    OTHER = 6


class BookingStatus(Enum):
    REQUESTED = 1
    PENDING = 2
    CONFIRMED = 3
    CHECKED_IN = 4
    CHECKED_OUT = 5
    CANCELLED = 6
    ABANDONED = 7


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5


class AccountType(Enum):
    MEMBER, GUEST, MANAGER, RECEPTIONIST = 1, 2, 3, 4


class PaymentStatus(Enum):
    UNPAID = 1
    PENDING = 2
    COMPLET = 3
    FILLED = 4
    DECLINE = 5
    CANCELL = 6
    ABANDON = 7
    SETTLIN = 8
    SETTLED = 9
    REFUNDED = 10
