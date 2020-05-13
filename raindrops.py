def raindrops(num):

    word = ""

    if num % 3 == 0:
        word = "Pling"
    if num % 5 == 0:
        word += "Plang"
    if num % 7 == 0:
        word +="Plong"
    if word == "":
        word = str(num)
    print(word)

raindrops(300)
raindrops(1755)
raindrops(9)
raindrops(34)
raindrops(7)
