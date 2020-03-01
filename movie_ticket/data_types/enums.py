#!/usr/bin/env python3

from enum import Enum


class BookingStatus(Enum):
    REQUESTED = 1
    PENDING = 2
    CONFIRMED = 3
    CHECKED_IN = 4
    CANCELED = 5
    ABANDONED = 6


class SeatType(Enum):
    REGULAR = 1
    PREMIUM = 2
    ACCESSIBLE = 3
    SHIPPED = 4
    EMERGENCY_EXIT = 5
    OTHER = 6


class AccountStatus(Enum):
    ACTIVE = 1
    BLOCKED = 2
    BANNED = 3
    COMPROMISED = 4
    ARCHIVED = 5
    UNKNOWN = 6


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
