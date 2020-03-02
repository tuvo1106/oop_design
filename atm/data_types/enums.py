#!/usr/bin/env python3

from enum import Enum


class TransactionType(Enum):
    BALANCE_INQUIRY = 1
    DEPOSIT_CASH = 2
    DEPOSIT_CHEC = 3
    WITHDRAW = 4
    TRANSFER = 5


class TransactionStatus(Enum):
    SUCCESS, FAILURE, BLOCKED, FULL, PARTIAL, NONE = 1, 2, 3, 4, 5, 6


class CustomerStatus(Enum):
    ACTIVE = 1
    BLOCKED = 2
    BANNED = 3
    COMPROMISED = 4
    ARCHIVED = 5
    CLOSED = 6
    UNKNOWN = 7
