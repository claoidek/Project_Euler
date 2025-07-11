# Finds the word in the file external_files/098_words.txt that can be mapped to
# the largest square by replacing letters with digits, that also has an anagram
# in the same file, which is mapped to a different square using the same
# mapping.

import time
from csv import reader
from itertools import combinations
from math import sqrt

def is_anagram(word1,word2):
    return sorted(word1) == sorted(word2)

# Returns a numerical representation of the input string where each letter is
# represented by a different number
# Example: "LETTER" -> [0, 1, 2, 2, 1, 3]
def pattern(string):
    output = []
    done = set()
    marker = 0
    for char in string:
        if char in done:
            output.append(output[string.index(char)])
        else:
            output.append(marker)
            marker += 1
        done.add(char)
    return tuple(output)

# Takes in an anamgram pair and returns a tuple representing how the first maps
# to the second
# Example: pattern("SHEET") = [0, 1, 2, 2, 3]
#          => mapping("SHEET","THESE") = [3, 1, 2, 0, 2]
def mapping(word1,word2):
    word1_pattern = pattern(word1)
    return tuple(word1_pattern[word1.index(x)] for x in word2)

start = time.time()

with open('external_files/098_words.txt', 'rt') as f:
    words = list(reader(f))[0]

words_by_length=[]
anagram_pairs = []

for i in range(len(max(words, key=len))):
    words_by_length.append([])

# Divides words by length
for word in words:
    words_by_length[len(word)-1].append(word)

# Finds all anagrams in the file
for word_set in words_by_length:
    for word1,word2 in combinations(word_set,2):
        if is_anagram(word1,word2):
            anagram_pairs.append([word1,word2])

# Finds set of lengths of all anagrams
lengths = set()
for word1,word2 in anagram_pairs:
    lengths.add(len(word1))

squares = []
squares_by_length = []
squares_with_anagram = []
valid_squares = []
square_keys = {}
square_pairs = []

# Calculate all squares up to the maximum needed
for i in range(int(sqrt(10**max(lengths)))):
    squares.append(i*i)

# Counts squares by their constituent digits
for square in squares:
    key = tuple(sorted(str(square)))
    if key in square_keys:
        square_keys[key] += 1
    else:
        square_keys[key] = 1

# Every square that shares the same constituent digits with another has an
# anagram
for square in squares:
    key = tuple(sorted(str(square)))
    if square_keys[key] > 1:
        squares_with_anagram.append(square)

# Finds all patterns of words with anagrams
valid_patterns = set()
for word1,word2 in anagram_pairs:
    valid_patterns.add(pattern(word1))
    valid_patterns.add(pattern(word2))

# Finds all squares that match the pattern of a word with an anagram
for square in squares_with_anagram:
    if pattern(str(square)) in valid_patterns:
        valid_squares.append(square)

# Divide squares by length
for i in range(len(max([str(x) for x in valid_squares], key=len))):
    squares_by_length.append([])
for square in valid_squares:
    squares_by_length[len(str(square))-1].append(square)

# Find squares with anagrams where both match a pattern of a word with an
# anagram
# Both permutations are added because we don't know which number will map to
# which word
for square_set in squares_by_length:
    for num1,num2 in combinations(square_set,2):
        if is_anagram(str(num1),str(num2)):
            square_pairs.append([num1,num2])
            square_pairs.append([num2,num1])

# Finds all mappings between anagrams
mapping_set = set()
for word1,word2 in anagram_pairs:
    mapping_set.add(mapping(word1,word2))

# Finds all pairs of squares that match the mapping between an anagram pair
square_anagrams = []
for num1,num2 in square_pairs:
    if mapping(str(num1),str(num2)) in mapping_set:
        square_anagrams.append([num1,num2])

# Finds the largest square remaining
max_square = 0
for pair in square_anagrams:
    if max(pair) > max_square:
        max_square = max(pair)

end = time.time()

print(max_square)
print("Time taken: ", end-start, "s", sep="")
