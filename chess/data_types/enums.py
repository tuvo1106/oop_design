#!/usr/bin/env python3

from enum import Enum


class GameStatus(Enum):
    ACTIVE = 1
    BLACK_WIN = 2
    WHITE_WIN = 3
    FORFEIT = 4
    STALEMATE = 5
    RESIGNATION = 6


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5
