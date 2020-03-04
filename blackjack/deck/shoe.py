#!/usr/bin/env python3

import random
from blackjack.deck.deck import Deck


class Shoe:
    def __init__(self, number_of_decks):
        self.__cards = []
        self.__number_of_decks = number_of_decks
        self.create_shoe()
        self.shuffle()

    def create_shoe(self):
        for _ in range(0, self.__number_of_decks):
            self.__cards.append(Deck().get_cards())

    def shuffle(self):
        card_count = len(self.__cards)
        for i in range(0, card_count):
            j = random.randrange(0, card_count - i - 1, 1)
            self.__cards[i], self.__cards[j] = self.__cards[j], self.__cards[i]

    # Get the next card from the shoe
    def deal_card(self):
        if len(self.__cards) == 0:
            self.create_shoe()
        return self.__cards.remove(0)
