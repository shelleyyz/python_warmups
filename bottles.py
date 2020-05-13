def bottles(num1,num2):

    for n in range(num1,num2,-1):

        if n == 2:

            print("2 bottles of beer on the wall, 2 bottles of beer.\nTake it down and pass it around, 1 bottle of beer on the wall")

        elif n == 1:

            print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall")

        elif n == 0:

            print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall")

        else:

            print(str(n) + " bottles of beer on the wall," + str(n) + " bottles of beer.\nTake one down, pass it around, " + str(n-1) + " bottles of beer on the wall")

bottles(99,-1)
bottles(60,20)
