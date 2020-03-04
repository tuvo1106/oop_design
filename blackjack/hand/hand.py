#!/usr/bin/env python3


class Hand:
    def __init__(self, blackjack_card1, blackjack_card2):
        self.__cards = [blackjack_card1, blackjack_card1]

    def get_scores(self):
        totals = [0]
        for card in self.__cards:
            new_totals = []
            for score in totals:
                new_totals.append(card.face_value() + score)
                if card.face_value() == 1:
                    new_totals.append(11 + score)
            totals = new_totals
        return totals

    def add_card(self, card):
        self.__cards.append(card)

    # get highest score which is less than or equal to 21
    def resolve_score(self):
        scores = self.get_scores()
        best_score = 0
        for score in scores:
            if score <= 21 and score > best_score:
                best_score = score
        return best_score
