def scrabble(word):

    score = 0

    letters = word.upper()

    for l in letters:

        if l in "A, E, I, O, U, L, N, R, S, T":

            score += 1

        if l in "D, G":

            score += 2

        if l in "B, C, M, P":

            score += 3

        if l in "F, H, V, W, Y":

            score += 4

        if l in "K":

            score += 5

        if l in "J, X":

            score += 8

        if l in "Q, Z":

            score += 10

    print(score)

scrabble("cabbage")
#working on the nested loop version
