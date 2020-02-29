#!/usr/bin/env python3

from enum import Enum


class QuestionStatus(Enum):
    OPEN, CLOSED, ON_HOLD, DELETED = 1, 2, 3, 4


class QuestionClosingRemark(Enum):
    DUPLICATE = 1
    OFF_TOPIC = 2
    TOO_BROAD = 3
    NOT_CONSTRUCTIVE = 4
    NOT_A_REAL_QUESTION = 5
    PRIMARILY_OPINION_BASED = 6


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5
