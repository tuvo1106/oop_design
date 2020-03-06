#!/usr/bin/env python3

from enum import Enum


class ReservationStatus(Enum):
    REQUESTED = 1
    PENDING = 2
    CONFIRMED = 3
    CHECKED_IN = 4
    CANCELED = 5
    ABANDONED = 6


class SeatType(Enum):
    REGULAR, KID, ACCESSIBLE, OTHER = 1, 2, 3, 4


class OrderStatus(Enum):
    RECEIVED, PREPARING, COMPLETED, CANCELED, NONE = 1, 2, 3, 4, 5


class TableStatus(Enum):
    FREE, RESERVED, OCCUPIED, OTHER = 1, 2, 3, 4


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5


class PaymentStatus(Enum):
    UNPAID = 1
    PENDING = 2
    COMPLETED = 3
    FILLED = 4
    DECLINED = 5
    CANCELLED = 6
    ABANDONED = 7
    SETTLING = 8
    SETTLED = 9
    REFUNDED = 10
