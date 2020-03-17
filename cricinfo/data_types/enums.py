#!/usr/bin/env python3

from enum import Enum


class MatchFormat(Enum):
    ODI, T20, TEST = 1, 2, 3


class MatchResult(Enum):
    LIVE, FINISHED, DRAWN, CANCELLED = 1, 2, 3, 4


class UmpireType(Enum):
    FIELD, RESERVED, TV = 1, 2, 3


class WicketType(Enum):
    BOLD = 1
    CAUGHT = 2
    STUMPED = 3
    RUN_OUT = 4
    LBW = 5
    RETIRED_HURT = 6
    HIT_WICKET = 7
    OBSTRUCTING = 8


class BallType(Enum):
    NORMAL, WIDE, WICKET, NO_BALL = 1, 2, 3, 4


class RunType(Enum):
    NORMAL, FOUR, SIX, LEG_BYE, BYE, NO_BALL, OVERTHROW = 1, 2, 3, 4, 5, 6, 7
