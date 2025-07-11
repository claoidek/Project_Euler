# Calculates the number of characters needed to write the numbers 1 to 1000 in words

import time

start = time.time()

# Occurences of each word
letter_counts = {
        # 100 for the numbers beginning with "one hundred ..."
        # 10x9 = 90 for numbers ending in "one"
        # 1 for the number "one thousand"
        # 100 + 90 + 1 = 191
        "one":191,
        # All of the following have the same number as "one", apart from the
        # extra occurence in "one thousand"
        "two":190,
        "three":190,
        "four":190,
        "five":190,
        "six":190,
        "seven":190,
        "eight":190,
        "nine":190,
        # All of the following occur once in every 100 numbers -> 10
        "ten":10,
        "eleven":10,
        "twelve":10,
        "thirteen":10,
        "fourteen":10,
        "fifteen":10,
        "sixteen":10,
        "seventeen":10,
        "eighteen":10,
        "nineteen":10,
        # All of the following occur ten times in every 100 numbers -> 100
        "twenty":100,
        "thirty":100,
        "forty":100,
        "fifty":100,
        "sixty":100,
        "seventy":100,
        "eighty":100,
        "ninety":100,
        # Appears once in every number from "one hundred" on -> 900
        "hundred":900,
        # Appears once
        "thousand":1,
        # Appears once in every number that contains "hundred" -> 900
        # But not the nine numbers "one hundred", "two hundred", etc. -> -9
        # 900 - 9 = 891
        "and":891
    }

characters = 0

for word in letter_counts:
    characters += len(word)*letter_counts[word]

end = time.time()

print(characters)
print("Time taken: ", end-start, "s", sep="")
