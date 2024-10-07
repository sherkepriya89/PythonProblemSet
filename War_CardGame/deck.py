from card import suits, ranks, Card, random
from random import shuffle

class Deck:
    """
    A class representing a deck of cards.
    
    Attributes:
    ----------
    all_cards : list
        A list containing all the cards in the deck.
    """

    def __init__(self):
        """
        Initializes the deck by creating a list of 52 Card objects, 
        one for each combination of suit and rank.
        """
        self.all_cards = []  # List to hold all the cards in the deck
        # Loop through each suit and rank to create the deck of cards
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)  # Create a card object
                self.all_cards.append(created_card)  # Add the card to the deck

    def shuffle(self):
        """
        Shuffles the deck of cards randomly.
        """
        random.shuffle(self.all_cards)  # Shuffle the cards in place

    def deal_one(self):
        """
        Deals a single card from the deck (removes and returns the last card).
        
        Returns:
        -------
        Card
            The last card from the deck list.
        """
        return self.all_cards.pop()  # Remove and return the last card in the deck

# Testing the deck functionality

# Create a new deck of cards
new_deck = Deck()

# Print the last card in the deck before shuffling (should be the last card added)
print(new_deck.all_cards[-1])

# Shuffle the deck
new_deck.shuffle()

# Print the last card in the deck after shuffling to verify it's randomized
print(new_deck.all_cards[-1])

# Deal one card (remove it from the deck) and print it
print(new_deck.deal_one())

# Print the number of remaining cards in the deck after dealing one
print(len(new_deck.all_cards))
