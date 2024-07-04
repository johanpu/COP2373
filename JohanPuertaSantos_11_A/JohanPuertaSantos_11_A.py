# This program simulates dealing a poker hand and allows the user to replace selected cards. It will
# then display the final hand.

import random


class Deck:
    def __init__(self, n_decks=1):
        self.card_list = [num + suit
                          for suit in '\u2665\u2666\u2663\u2660'
                          for num in 'A23456789TJQK'
                          for deck in range(n_decks)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    # Book used this method for deal, not sure why if only one hand is used?
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

    # Replaces the cards in the hand with new cards.
    def replace_cards(self, cards_to_replace):
        for card in cards_to_replace:
            self.cards_in_play_list.remove(card)
            self.discards_list.append(card)
            self.deal()


def simulate_replacement():
    # Deals a hand of 5 cards.
    deck = Deck(1)  # Uses a single deck of 52 cards.
    hand_size = 5
    hand = [deck.deal() for _ in range(hand_size)]

    print(f"Initial hand: {hand}")

    # Asks user for cards to replace (must be between 1 -5.)
    cards_to_replace = input("Enter the positions of cards to replace (separated by commas, from 1 - 5): ")
    cards_to_replace = [int(pos) - 1 for pos in cards_to_replace.split(',') if pos.strip().isdigit()]

    # Ensures valid input and replaces the cards.
    if all(0 <= pos < hand_size for pos in cards_to_replace):
        for pos in sorted(cards_to_replace, reverse=True):
            deck.replace_cards([hand[pos]])
            hand[pos] = deck.cards_in_play_list[-1]  # Get the last dealt card
        print(f"Final hand: {hand}")
    else:
        print("\nInvalid position(s) entered. No cards replaced.")


if __name__ == "__main__":
    simulate_replacement()
