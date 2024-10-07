# player.py

from card import suits, ranks, Card  # Import suits, ranks, and Card class from card module
from deck import Deck  # Import the Deck class from deck module

class Player:
    """
    A class representing a player in the card game.
    
    Attributes:
    ----------
    name : str
        The name of the player.
    all_cards : list
        The list of cards the player currently holds.
    """
    
    def __init__(self, name):
        """
        Initialize a player with a name and an empty list of cards.
        
        Parameters:
        ----------
        name : str
            The player's name.
        """
        self.name = name
        self.all_cards = []  # List to hold the player's cards

    def remove_one(self):
        """
        Removes and returns the first card from the player's list of cards.
        
        Returns:
        -------
        Card
            The card at the front of the player's hand.
        """
        return self.all_cards.pop(0)  # Remove the card from the top (front)

    def add_cards(self, new_cards):
        """
        Adds one or more cards to the player's list of cards.
        
        Parameters:
        ----------
        new_cards : list or Card
            Either a single card or a list of cards to add to the player's hand.
        """
        if isinstance(new_cards, list):  # If new_cards is a list, extend the player's hand
            self.all_cards.extend(new_cards)
        else:  # If it's a single card, append it to the player's hand
            self.all_cards.append(new_cards)

    def __str__(self):
        """
        Returns a string representation of the player and the number of cards they hold.
        
        Returns:
        -------
        str
            A description of the player and how many cards they have.
        """
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# Create a new deck and shuffle it
new_deck = Deck()  # Create a new deck of cards
new_deck.shuffle()  # Shuffle the deck randomly

# GAME SETUP

# Create two players: Player One and Player Two
player_one = Player("One")
player_two = Player("Two")

# Deal 26 cards to each player from the shuffled deck
for x in range(26):
    player_one.add_cards(new_deck.deal_one())  # Give one card to Player One
    player_two.add_cards(new_deck.deal_one())  # Give one card to Player Two

# Test the game setup by printing the number of cards each player has
print(player_one)
print(player_two)

# Variable to control the game flow
game_on = True
round_num = 0  # Keep track of the number of rounds

# Main game loop
while game_on:
    round_num += 1  # Increment round number
    print(f"Round {round_num}")

    # Check if any player is out of cards
    if len(player_one.all_cards) == 0:
        print('Player One is out of cards! Player Two Wins!')
        game_on = False  # End the game
        break
    elif len(player_two.all_cards) == 0:
        print('Player Two is out of cards! Player One Wins!')
        game_on = False  # End the game
        break

    # Start a new round by having each player place one card
    player_one_cards = [player_one.remove_one()]  # Player One places one card
    player_two_cards = [player_two.remove_one()]  # Player Two places one card

    # Enter a loop to handle "war" situations
    at_war = True
    while at_war:
        # Compare the values of the last card each player placed
        if player_one_cards[-1].value > player_two_cards[-1].value:
            # Player One wins this round and takes both piles of cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False  # End the war
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            # Player Two wins this round and takes both piles of cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False  # End the war
        else:
            # If the cards have the same value, a "war" begins
            print('War!')

            # Check if either player has insufficient cards to declare war
            if len(player_one.all_cards) < 5:
                print('Player One unable to declare war')
                print('Player Two Wins!')
                game_on = False  # End the game
                break
            elif len(player_two.all_cards) < 5:
                print('Player Two unable to declare war')
                print('Player One Wins!')
                game_on = False  # End the game
                break
            else:
                # Each player places 5 cards (3 face down and 1 face up for war)
                for _ in range(5):
                    player_one_cards.append(player_one.remove_one())  # Player One adds cards to the pile
                    player_two_cards.append(player_two.remove_one())  # Player Two adds cards to the pile
