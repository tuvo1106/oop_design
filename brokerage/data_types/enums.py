#!/usr/bin/env python3

from enum import Enum


class ReturnStatus(Enum):
    SUCCESS = 1
    FAIL = 2
    INSUFFICIENT_FUNDS = 3
    INSUFFICIENT_QUANTITY = 4
    NO_STOCK_POSITION = 5


class OrderStatus(Enum):
    OPEN, FILLED, PARTIALLY_FILLED, CANCELLED = 1, 2, 3, 4


class TimeEnforcementType(Enum):
    GOOD_TILL_CANCELLED = 1
    FILL_OR_KILL = 2
    IMMEDIATE_OR_CANCEL = 3
    ON_THE_OPEN = 4
    ON_THE_CLOSE = 5


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5
