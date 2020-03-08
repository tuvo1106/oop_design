#!/usr/bin/env python3

from chess.player.account import Account


class Player(Account):
    def __init__(self, person, white_side=False):
        self.__person = person
        self.__white_side = white_side

    def is_white_side(self):
        return self.__white_side
