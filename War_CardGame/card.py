
import random  # Importing random module for future use (e.g., shuffling a deck)

# Define the four suits in a deck of cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# Define the ranks of cards in a deck, from Two to Ace
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Assign values to each rank of card
# Note: Values are important for comparing cards in games like War
values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 
    'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
}

class Card:
    """
    A class representing a single playing card.
    
    Attributes:
    -----------
    suit : str
        The suit of the card (e.g., Hearts, Diamonds, etc.).
    rank : str
        The rank of the card (e.g., Two, Three, Ace, etc.).
    value : int
        The value of the card based on its rank, used for comparisons.
    """
    def __init__(self, suit, rank):
        """
        Initialize the card with a suit and a rank, and derive its value.
        
        Parameters:
        -----------
        suit : str
            The suit of the card (e.g., Hearts, Spades).
        rank : str
            The rank of the card (e.g., Ace, Two, King).
        """
        self.suit = suit  # The suit of the card (Hearts, Spades, etc.)
        self.rank = rank  # The rank of the card (Two, Ace, etc.)
        self.value = values[rank]  # The value of the card, derived from the rank

    def __str__(self):
        """
        Return a string representation of the card (rank + suit).
        
        Returns:
        --------
        str
            The human-readable description of the card.
        """
        return self.rank + " of " + self.suit  # Format the card as "Rank of Suit"


# Example of creating a card: Two of Hearts
two_hearts = Card("Hearts", "Two")

# Test: Print the value of the Two of Hearts card (should be 2)
print(two_hearts.value)
