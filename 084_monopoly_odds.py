# Finds the three most likely squares to land on in a game of Monopoly using two
# four-sided dice

# List of squares and their indices
# More details at https://projecteuler.net/problem=84
#   0   GO
#   1   A1
#   2   CC1
#   3   A2
#   4   T1
#   5   R1
#   6   B1
#   7   CH1
#   8   B2
#   9   B3
#   10  JAIL
#   11  C1
#   12  U1
#   13  C2
#   14  C3
#   15  R2
#   16  D1
#   17  CC2
#   18  D2
#   19  D3
#   20  FP
#   21  E1
#   22  CH2
#   23  E2
#   24  E3
#   25  R3
#   26  F1
#   27  F2
#   28  U2
#   29  F3
#   30  G2J
#   31  G1
#   32  G2
#   33  CC3
#   34  G3
#   35  R4
#   36  CH3
#   37  H1
#   38  T2
#   39  H2

from time import clock
import random

# Draws a card a puts it at the bottom of the deck
# Doesn't shuffle the deck after going through all cards
def draw_card(deck):
    deck.insert(15,deck.pop(0))
    return deck[15]

def roll_dice():
    return [random.randint(1,dice_sides),random.randint(1,dice_sides)]

# Community Chest cards
def CC_outcome(square,card):
    if card == 0:
        return square
    if card == 1:
        return 0
    if card == 2:
        return 10

# Chance cards
def CH_outcome(square,card):
    if card == 0:
        return square
    if card == 1:
        return 0
    if card == 2:
        return 10
    if card == 3:
        return 11
    if card == 4:
        return 24
    if card == 5:
        return 39
    if card == 6:
        return 5
    if card in [7,8]:
        while square not in R:
            square = (square + 1)%40
        return square
    if card == 9:
        while square not in U:
            square = (square + 1)%40
        return square
    if card == 10:
        return square - 3
    
start = clock()

dice_sides = 4

# Community Chest squares
CC = [2,17,33]
# Chance Squares
CH = [7,22,36]
# Railway Stations
R = [5,15,25,35]
# Utilities
U = [12,28]
# Go to Jail
G2J = [30]

CC_cards = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2]
CH_cards = [0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,10]
random.shuffle(CC_cards)
random.shuffle(CH_cards)

consecutive_doubles = 0
landed_on = [0]*40
square = 0
# The number of turns can be reduced to reduce the runtime, but since the answer
# is probabilty-based, the more terms the better for accuracy
turns = 1000000
end_turn = False

for i in range(turns):
    d1,d2 = roll_dice()
    # Sends you to jail if three doubles are rolled in a row
    if d1 == d2:
        consecutive_doubles += 1
        if consecutive_doubles == 3:
            consecutive_doubles = 0
            square = 10
            end_turn = True
    else:
        consecutive_doubles = 0

    if not end_turn:
        square = (square + d1 + d2)%40
        if square in CC:
            card = draw_card(CC_cards)
            square = CC_outcome(square,card)
        elif square in CH:
            card = draw_card(CH_cards)
            square = CH_outcome(square,card)
        elif square in G2J:
            square = 10

    landed_on[square] += 1
    end_turn = False

end = clock()

print "".join([str(x) for x \
        in sorted(range(len(landed_on)),key=lambda i:-landed_on[i])[:3]])
print "Time taken: ", end-start, " s"
