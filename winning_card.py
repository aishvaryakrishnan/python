# In a card game, each player will be given a set of random cards. Players will throw on the table their one winning card, the player with the highest card wins.
# A winning card is the card that only exists once in the set of cards, and the highest one.
# Given an array of sets of integers cards, return the card of the winning player. Return -1 If no such card is found.

import sys

def winning_card(cards : list) -> int:

    res = -1
    
    for player_cards in cards:
        sorted_player_cards = sorted(player_cards, reverse=True)
        
        for card in sorted_player_cards:
            if card == res:
                res = -1
            elif card > res:
                res = card
                
    return res


cards_input = input("enter all the players' cards (space-separated for each player and comma-separated for different players. Example: \"1 2, 5 5\" ) \n")
all_player_cards = ((int(player_card) for player_card in player_cards.split(' ')) for player_cards in (card.strip() for card in cards_input.split(',')))

print(winning_card(all_player_cards))
