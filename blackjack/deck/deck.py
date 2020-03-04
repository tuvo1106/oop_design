#!/usr/bin/env python3

import datetime
from blackjack.card.blackjack_card import BlackjackCard
from blackjack.data_types.enums import SUIT


class Deck:
    def __init__(self):
        self.__cards = []
        self.__creation_date = datetime.date.today()
        for value in range(1, 14):
            for suit in SUIT:
                self.__cards.append(BlackjackCard(suit, value))

    def get_cards(self):
        self.__cards
