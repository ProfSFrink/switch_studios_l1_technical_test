# SWITCH STUDIOS TECHNICAL TEST

**AUTHOR:** _Steven Partlow_ <<stevenpartlow@outlook.com>>
**DATE:** _04/02/2024_

## 1. INTRODUCTION

This is my submission of the Switch Studios technical test, for the position of Game Developer Level 1.

## 2. ABOUT THE PROGRAM - THE POKERMATIC 9000

I have submitted this program as a Python script, I developed the program in Jupyter Notebook, as this made testing the program as I made it easier, I've submitted the notebook in addition to the _.py_ script. I have fully commented all the code to explain the way the program solves the problem.

I store the hand as a python list, while I did consider turning the cards in to objects for the purpose of this test, it added extra uneccesary steps to the program and seeing as the user specifies the hand of cards that we need to check, keeping the hand stored as a list made the most sense.

The program can idenifty all winning poker hands as specified in the project document so:

- High Card
- Pair
- Two Pair
- Three of a Kind
- Straight
- Flush
- Full House
- Four of a Kind
- Straight Flush
- Royal Flush

## 3. USING THE PROGRAM

The program expects the input in the same format as shown in the technical test pdf file, which is in the comma delimited format as shown below, with the card value coming before the suit type, then a comma.

``` 13H, 8C, 2S, 4H, 7D ```

Some things to note here:

- Aces are input as zero (0)
- Then the remaining card values are 2 through 10
  - Jacks are 11
  - Queens are 12
  - Kings are 13
- Suits are represented by their inital, so D (**Diamonds**), H (**Hearts**), S (**Spades**), and C (**Clubs**)
- There is no space between the card value and suit type

You do not have to include the space after the comma, as the program will still work without it, the letter for the suit can also be in lowercase. 

## 4. ERROR HANDLING

If you use more than one comma, when entering the input string, or any other character that is not a comma:

``` 13H, 8C, 2S,, 4H, 7D ```

The program will raise an exception if two commas appear in sequence, regular expressions are used detect this. The program will also raise an exception if any of the following errors occur:

- If the input string has the suit appear before the card value, eg. ``` H13 ```
- You enter a card value lower than zero, or higher than 13, eg. ``` 17D, 1S, 4H, 8H, 3C ```
- You enter an Ace as one, as the program expects them to input as zero, eg. ``` 10C, 11C, 12C, 13C, 1C ```
- You enter any other letter, other than the 4 ones that represent the suit names, eg. ``` 1X ```

Providing a valid hand is entered the program will tell the user what the value of the hand they have, the program will also display's some of the working it uses to check the hand.
