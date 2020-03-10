#!/usr/bin/env python3

from enum import Enum


class BillItemType(Enum):
    BASE_CHARGE, ADDITIONAL_SERVICE, FINE, OTHER = 1, 2, 3, 4


class VehicleLogType(Enum):
    ACCIDENT = 1
    FUELING = 2
    CLEANING_SERVICE = 3
    OIL_CHANGE = 4
    REPAIR = 5
    OTHER = 6


class VanType(Enum):
    PASSENGER, CARGO = 1, 2


class CarType(Enum):
    ECONOMY = 1
    COMPACT = 2
    INTERMEDIATE = 3
    STANDARD = 4
    FULL_SIZE = 5
    PREMIUM = 6
    LUXURY = 7


class VehicleStatus(Enum):
    AVAILABLE, RESERVED, LOANED, LOST, BEING_SERVICED, OTHER = 1, 2, 3, 4, 5, 6


class ReservationStatus(Enum):
    ACTIVE, PENDING, CONFIRMED, COMPLETED, CANCELLED, NONE = 1, 2, 3, 4, 5, 6


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
