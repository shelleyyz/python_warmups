def ask_shell(input):

    if "?" in input:
        print("Sure")

    elif input.isupper() == True:
        print("Chill out dude")

    elif input == "":
        print("Fine, be an a-hole")

    else:
        print("Whatever bitch")

ask_shell("")
ask_shell("Can I ask a question?")
ask_shell("YOU SUCK")
ask_shell("Don't know")
