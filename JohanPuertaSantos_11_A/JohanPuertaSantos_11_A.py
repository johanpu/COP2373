# This program simulates dealing a poker hand and allows the user to replace selected cards. It will
# then display the final hand.

import random


class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("Reshuffling Deck...")
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


def hand():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    my_deck = Deck(52)

    for i in range(12):
        for i in range(5):
            d = my_deck.deal()
            r = d % 13
            s = d // 13
            print(ranks[r], "of", suits[s])
        print()

