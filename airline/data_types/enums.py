#!/usr/bin/env python3

from enum import Enum


class FlightStatus(Enum):
    ACTIVE = 1
    SCHEDULED = 2
    DELAYED = 3
    DEPARTED = 4
    LANDED = 5
    IN_AIR = 6
    ARRIVED = 7
    CANCELLED = 8
    DIVERTED = 9
    UNKNOWN = 10


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


class ReservationStatus(Enum):
    REQUESTED = 1
    PENDING = 2
    CONFIRMED = 3
    CHECKED_IN = 4
    CANCELLED = 5
    ABANDONED = 6


class SeatClass(Enum):
    ECONOMY = 1
    ECONOMY_PLUS = 2
    PREFERRED_ECONOMY = 3
    BUSINESS = 4
    FIRST_CLASS = 5


class SeatType(Enum):
    REGULAR, ACCESSIBLE, EMERGENCY_EXIT, EXTRA_LEG_ROOM = 1, 2, 3, 4


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5
