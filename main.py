import random


def scrabble_word(u_word):
    s_dictionary = {
        "E": 1, "A": 1, "I": 1, "O": 1, "N": 1, "R": 1, "T": 1, "L": 1, "S": 1, "U": 1,
        "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10,
    }

    score = 0
    for i in u_word.upper():  # i = G
        letter = s_dictionary[i]
        score += letter

    return score


eng_alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                 "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for i in range(0, 11):
    eng_alphabets.append("E")

for j in range(0, 8):
    eng_alphabets.append("A")
    eng_alphabets.append("I")

for k in range(0, 7):
    eng_alphabets.append("O")

for l in range(0, 5):
    eng_alphabets.append("N")
    eng_alphabets.append("R")
    eng_alphabets.append("T")

# for l in range(0, 5):

# 4 tiles	L, S, U, D
# 3 tiles	G
# 2 tiles	B, C, M, P, F, H, V, W, Y
# 1 tile	K, J, X, Q, Z


p_rack = [random.choice(eng_alphabets) for n in range(0, 7)]

print(scrabble_word("guardian"))
print(p_rack)
