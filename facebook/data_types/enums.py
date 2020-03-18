#!/usr/bin/env python3

from enum import Enum


class ConnectionInvitationStatus(Enum):
    PENDING, ACCEPTED, REJECTED, CANCELED = 1, 2, 3, 4


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, DISABLED = 1, 2, 3, 4, 5
