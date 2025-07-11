# Reads in a set of pairs of poker hands from external_files/054_poker.txt and
# determines how many of them player 1 wins

import csv
import time

def hand_identifier(cards):
    # Map for converting all cards to a numeric value
    mapping = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13}
    
    # Stores the rank of the hand:
    # 0 - Royal Flush
    # 1 - Straight Flush
    # 2 - Four of a Kind
    # 3 - Full House
    # 4 - Flush
    # 5 - Straight
    # 6 - Three of a Kind
    # 7 - Two Pairs
    # 8 - One Pair
    # 9 - High Card
    rank = 999

    # These three store tie-breaking values for each hand
    # What exactly these are depends on the kind of hand
    # Tie-breaking is done in the order tie1>tie2>reversed(kickers)
    # kickers defaults to [0,0,0,0,0] and tie1,tie2 to 0 unless stated otherwise
    # Royal Flush       - N/A
    # Straight Flush    - kickers = [Card values in ascending order] 
    # Four of a kind    - kickers = [0,0,0,0, value of singleton card] 
    #                   - tie1 = common value of the other four cards
    # Full House        - tie1 = common value of the three cards
    #                   - tie2 = common value of the other two cards
    # Flush             - kickers = [Card values in ascending order]
    # Straight          - kickers = [Card values in ascending order]
    # Three of a Kind   - kickers = [0,0,0, lower singleton, higher singleton]
    #                   - tie1 = common value of the other three cards
    # Two Pairs         - kickers = [0,0,0,0, value of unpaired card]
    #                   - tie1 = higher pair
    #                   - tie2 = lower pair
    # One Pair          - kickers = [0,0, lowest singleton, middle singleton, highest singleton]
    #                   - tie1 = common value of pair
    # High Card         - kickers = [Card values in ascending order]
    kickers = [0,0,0,0,0]
    tie1 = 0
    tie2 = 0

    suit = cards[0][1]
    values = []
    suited = True
    for card in cards:
        values.append(mapping[card[0]])
        # Suiting only matters if all cards have the same suit
        if card[1] is not suit:
            suited = False

    svalues = sorted(values)
    same = svalues.count(most_common(svalues))

    if suited:
        # Royal Flush
        if svalues == [1,10,11,12,13]:
            rank = 0
            tie1 = 0
            tie2 = 0
        # Straight Flush
        elif svalues[4]-svalues[0]==4:
            rank = 1
            tie1 = 0
            tie2 = 0
            kickers = svalues
        # Flush
        else:
            rank = 4
            tie1 = 0
            tie2 = 0
            kickers = svalues

    # Four of a Kind
    elif same == 4:
        rank = 2
        tie1 = svalues[2]
        tie2 = 0
        kickers[4] = least_common(svalues)

    elif same == 3:
        # Full House
        if svalues.count(least_common(svalues)) == 2:
            rank = 3
            tie1 = svalues[2]
            tie2 = least_common(svalues)
        # Three of a Kind
        else:
            rank = 6
            tie1 = svalues[2]
            tie2 = 0
            if svalues[4] != tie1:
                kickers[4] = svalues[4]
                if svalues[3] != tie1:
                    kickers[3] = svalues[3]
                else:
                    kickers[3] = svalues[0]
            else:
                kickers[4] = svalues[1]
                kickers[3] = svalues[0]
            if kickers[3] == 1:
                kickers[3], kickers[4] = kickers[4], kickers[3]

    # Straight
    elif (len(svalues)==len(set(svalues))) and (svalues[4]-svalues[0]==4 or svalues == [1,10,11,12,13]):
        rank = 5
        tie1 = 0
        tie2 = 0
        kickers = svalues

    elif same == 2:
        # Two Pairs
        if len(set(svalues)) == 3:
            rank = 7
            if svalues.count(svalues[0]) == 1:
                tie1 = svalues[4]
                tie2 = svalues[2]
                kickers[4] = svalues[0]
            elif svalues.count(svalues[2]) == 1:
                tie1 = svalues[4]
                tie2 = svalues[1]
                kickers[4] = svalues[2]
            else:
                tie1 = svalues[3]
                tie2 = svalues[1]
                kickers[4] = svalues[4]
        # One Pair
        else:
            rank = 8
            for i in range(4,-1,-1):
                if svalues.count(svalues[i]) == 1:
                    kickers[i] = svalues[i]
                else:
                    tie1 = svalues[i]
                tie2 = 0
    # High Card
    else:
        rank = 9
        tie1 = 0
        tie2 = 0
        kickers = svalues

    # Adjust Aces to be worth 14 in tie-breakers
    for index,kicker in enumerate(kickers):
        if kicker == 1:
            kickers[index] = 14
    kickers.sort()
    if tie2 == 1:
        tie2 = 14
    if tie1 == 1:
        tie1 = 14

    return rank, tie1, tie2, kickers

def least_common(lst):
        return min(set(lst), key=lst.count)

def most_common(lst):
        return max(set(lst), key=lst.count)

start = time.time()

count = 0

with open('external_files/054_poker.txt', 'r') as f:
    hands = csv.reader(f, delimiter=' ')

    for hand in hands:
        ranka,tie1a,tie2a,kickersa = hand_identifier(hand[:5])
        rankb,tie1b,tie2b,kickersb = hand_identifier(hand[5:])
        if ranka != rankb:
            count += ranka<rankb
            continue
        if tie1a != tie1b:
            count += tie1a>tie1b
            continue
        if tie2a != tie2b:
            count += tie2a>tie2b
        for i in range(4,-1,-1):
            if kickersa[i] != kickersb[i]:
                count += kickersa[i]>kickersb[i]
                break
        
end = time.time()

print(count)
print("Time taken: ", end-start, "s", sep="")
