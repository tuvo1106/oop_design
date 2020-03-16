#!/usr/bin/env python3

from enum import Enum


class ConnectionInvitationStatus(Enum):
    PENDING, ACCEPTED, CONFIRMED, REJECTED, CANCELED = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6
