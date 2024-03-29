"""
Switch Studios Developer L1 Technical Test
The PokerMatic 9000

AUTHOR: Steven Partlow <stevenpartlow@outlook.com>
DATE: 01/02/2024
VERSION: 1.0

I have developed this program to follow the exact
specification as in the inital document
"""

def check_hand(hand):
    """
    Functions to check a passed in hand to see if it's a winning one
    """

    # A dictionary to define numerical values to each of the card values
    # this will assign a numerical values to the values stated in our
    # input string, the zip function will use these key value pairs
    # as a base
    #
    # card_value = {
    # "2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7,
    # "10": 8, "11": 9, "12": 10, "13": 11, "0": 12
    # }
    #
    # We use the zip method to match the string values from our comma
    # delimted string, to a range of integers going from zero to 13,
    # the values are off by 2 for now we will adjust this later,
    # we now have a dictionary of k/v pairs of our hand of cards

    card_value = dict(zip('2 3 4 5 6 7 8 9 10 11 12 13 0'.split(), range(14)))

    # A list of strings, representing our valid suits
    valid_suits = ["D","H","C","S"]

    cards = [] # An empty list for the values of our cards
    suits = [] # An empty list for the suits of our cards

    for card in hand:
        # Iterate through the hand of cards

        c = card[:-1] # 'c' will be the first / second characters, the value of our card
        s = card[-1:].upper() # 's' will be the last character, the suit of our card,
                              # we convert to uppercase, to account if entered in lowercase

        # The user may input an ace as a 1 instead of 0, this accounts for that
        if c == '1':
            raise ValueError("Aces must be entered as 0!")

        # We account for the card value not being a number
        # We attempt to convert the value of c to an integer if this fails
        # then we know the input is not a number and raise an exception
        if not type(int(c)) is int:
            raise TypeError("Card values must be entered as 0, or 2 to 13!")

        # We check that the value of s if one of the four suits and again
        # if not we raise an exception, will also error if not a character
        if s not in valid_suits:
            raise ValueError("Suit values must be entered as D, H, C or S!")

        cards.append(c) # add the value of 'c' to card values list
        suits.append(s) # add the value of 's' to suits list

    # We now have two lists of cards, one to of the values of our cards, and one
    # of the suits of our cards.

    # We check to make sure the hand is five cards, at the project document
    # specifies this

    if len(cards) != 5 and len(suits) != 5:
        raise ValueError("Your hand has less than 5 cards!")

    # Finally we have to check that the card values are within the valid ranges
    # 0 is allowed as this represents aces, and nothing under 2 or over 13

    for c in cards:
        if int(c) != 0 and int(c) < 2 or int(c) > 13 :
            raise ValueError("Card values must be entered as 0, or 2 to 13!")

    # We are now going to create three variables,
    # which we need to see if our hand is a winner

    # Firstly 'high_suit', which is the highest number of times any suit appears in our hand

    # For each indiviual suit in the 'suits' list we count the number of times
    # it occurs, we set 'high_suit' to be this value

    high_suit = max([suits.count(a) for a in suits])
    print(f"Max times one suit occurs is {high_suit}")

    # Next 'dup_cards', which counts how many times each value occurs

    # For each card in the 'cards' list, we count how many times each value repeats,
    # the length of the list tells us how many individual values we have, this list
    # is also sorted lowest to highest

    dup_cards = sorted([cards.count(a) for a in set(cards)])
    print(f"There is {len(dup_cards)} unique values in the hand, with each occuring {dup_cards}")

    # Next 'card_values', which is the numerical value of our cards

    # For each element in the 'cards' list, we take the value, which is a string
    # value, we then use that string value in our 'card_value' dictionary as a key and
    # take the matching value in the dictionary, we then use that as
    # the numerical value of the card, when then add two on two the value from the dictionary
    # here so the values now match, this list is also sorted lowest to highest.
    # Going forward our aces will now be 14.

    card_values = sorted([card_value[a]+2 for a in cards])

    print(f"The value of the cards in the hand is in ascending order is {card_values}")

    # ============== CHECK FOR WINNING HANDS ============== #

    def check_for_straight(card_values):
        """
        Function to check current card values and see if we have a straight
        """

        # Check the difference between the last value of the hand and the first
        diff = card_values[-1] - card_values[0]
        # If the difference is four
        if diff == 4:
            return True # Then we have a straight as we sorted the cards earlier
        # If the difference is tweleve (hand starts with a 2, ends with an Ace)
        elif diff == 12:
            # And the difference between the 2nd card and last card is 3
            # (we have a 2 through 5 in our hand)
            if card_values[-2] - card_values[0] == 3:
                # Because we start with a 2 through to 5, end with an ace, we
                # have a straight
                return True
        return False

    # We will check for winning hands in descending order so best to worst
    # Firstly we check for the highest value winning hands, the three flushes

    # If all five cards are the same suit, (One suit appeared 5 times in our hand)
    if high_suit == 5:
        if check_for_straight(card_values): # If we have a straight
            if card_values[0] == 10: # and the hand starts with an 10 we have a ROYAL FLUSH
                return "Royal Flush!"
            return "Straight Flush!" # If it does not start with a 10 then we have a STRAIGHT FLUSH
        return "Flush!" # If we only have one suit and no straight, then we have a FLUSH

    # Next we will check our duplicate cards
    # By checking the length of the dup_cards list, we know how many unique values we have
    # Two unqiue values means that we either have a two pairs or a full house
    elif len(dup_cards) == 2:
        # If one value occurs four times then we have...
        if max(dup_cards) == 4: # A FOUR OF A KIND
            return "Four of a Kind!"
        # If one value occurs three times then we have...
        elif max(dup_cards) == 3: # A FULL HOUSE
            return "Full House!"

    # Three unique values means that we either have a Three of a Kind or a Two Pair
    elif len(dup_cards) == 3:
        # If one value occurs three times then...
        if max(dup_cards) == 3: # We have a THREE OF A KIND
            return "Three of a Kind!"
        else: # If we don't have three unique values..
            return "Two Pair!" # We have a TWO PAIR

    # Four unique values means we either have just Pair, a Straight or a High Card
    elif len(dup_cards) == 4:
        return "Pair!"
    else: # We either have a High Card or a Straight
        # So we check for a straight
        if check_for_straight(card_values):
            return "Straight!" # If it returns true then we have a STRAIGHT
        return "High Card!" # If false then we just have a HIGH CARD

if __name__ == "__main__":
    # Main program

    import os # Import the os module
    os.system('clear') # This will clear the screen

    print("Welcome to the Pokermatic 9000")
    print("Version 1.0\n")
    print("The Pokermatic 9000 is program that must output the highest")
    print("poker rank that exists in an input string that represents")
    print("five standard playing cards.\n")

    print("You should input the hand as a comma delimited string\n")
    print("eg. 13H, 8C, 12D, 7H, 2S\n")
    print("Aces are input as 0")
    print("Ranks are 2 - 10, Jack is 11, Queen is 12, and King as 13")
    print("D for Diamonds, C for Clubs, H for Hearts, and S for Spades\n")
    print("Entering any other values will result in an error")
    print("Entering the values in the wrong sequence will also result")
    print("an error.\n")

    print("There should always be a ', ' between each card.\n")

    # The card values are represented as 2 through 10 for the numerical cards
    # 0 for Aces, 11 for Jacks, 12 for Queens and 13 for Kings
    # The suits are C is for Clubs, D for Diamonds, H for Hearts and S for Spades

    # A list of winning hands, one for each winning type of poker hand
    # Each hand is in comma delimted string containing five playing cards
    # seperated by ","

    # These lists are left over from when I was developing the program,
    # I would feed these into the check_hand function one after the other
    # to to check that the program was recognising the correct winning
    # hands and erroring out correctly, you can see the code I used for
    # this in the Jupyter noteboook

    winning_hands = [
        "13H, 8C, 12D, 7H, 2S", # A High card
         "0D, 2D, 3D, 4D, 5D", # Straight flush
         "0H, 10H, 11H, 12H, 13H", # Royal flush
         "13S, 10S, 8S, 7S, 5S", # Flush
         "13H, 13C, 13D, 13S, 8S", # Four of a kind
         "5C, 5D, 5S, 12C, 12H", # Full house
         "9H, 9C, 9D, 12H, 3C", # Three of a kind
         "3C, 9S, 9H, 5D, 5C", # Two pair
         "9S, 10H, 6C, 6S, 2D", # Pair
         "3S, 4H, 5D, 6C, 7H" # Straight
    ]

    error_hands = [
        "10C, 2D, 5H, 12C, 3S",
        "2S, 5D, 11D,, 3C, 13H",
        "10C, 3D, 5D, 4H, 6S"
    ]

    import re # Import the regular expressions module so we can check
          # the if the input string is in the correct comma delimted
          # format

    # The pattern to check our comma delimted string against the pattern
    # ignore any alphanumeric characters before the first ", "
    # then checks that it only is a comma and a space, before the pattern
    # continues, this ensures are values are divided by only one comma and
    # a space, we will validiate the rest of the input latter in the program
    pattern = re.compile(r"^(\w+)(,\s*\w+)*$")

    def check_valid_input(input_string):
        """ 
        A function to compare an input string against the above defined pattern
        returing true or false depending on the outcome        
        """
        if pattern.match(input_string) is None:
            return False
        else:
            return True

    # We have the variable Hand which is a list

    hand = input("Enter player hand: ")

    # We check if the input hand has been entered correctly, if it has...
    if check_valid_input(hand):
        # We take the current hand, then split the cards into indiviual elements, using the ', '
        # as our marker to split, this then gives us a 'player_hand' list, with each element
        # being one of our playing cards
        player_hand = [str(x) for x in hand.split(', ')]

        # Then pass it into our check_hand function, then output what is returned
        # the output is displayed using an f string

        print(f"With a hand of {hand}, Player has a {check_hand(player_hand)}!\n")

    else: # If the string is invalid we inform the user and raise an exception
        print("Invalid input hand")
        print("The input string is not in the correct format, it must be a number,")
        print("then a letter representing a valid suit (C, D, S, H) then a comma,")
        print("then a space and repeated five times!")
        print("Example: 9H, 9C, 9D, 12H, 3C\n")
        raise ValueError ("Invalid input hand!")
