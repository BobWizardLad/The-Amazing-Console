


def teamLuck():
    import art

    balance = 1000
    art.tprint("Welcome to the CASINO")
    print("Lets go get some MONEY$$$. SHEEESH")
    print("Your starting balance is", balance)
    print("Your goal is to get to 2,000")


    print("Slotmachine? (y/n)")
    decision = input()

    while (decision == "y"):
        import random
        wordList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "M", "N", "O","L", "L", "L", "L", "L"]
        n = 0
        slotList = []
        while (n < 3):
            x = random.randint(0, len(wordList) - 1)
            slotList += [wordList[x]]
            n += 1
        nonRepeatSlotList = set(slotList)

        if len(nonRepeatSlotList) == 1 and nonRepeatSlotList != ("L"):
            print("YOU WIN")
            balance += 1000
        elif nonRepeatSlotList == ("L"):
            print("MASSSSSIVE L BRUH")

            balance -= 100000000000000000000000000000000000000000000000000000

        else:
            print("Did you know that 99% of gamblers quit before their first big win?")
            balance -= 250
        for a in slotList:
            art.tprint(a, font = 'block', chr_ignore = True)

        print("Would you like to keep going?")
        print(balance)
        decision = input()
    if (decision == "n"):
        print("You are not smart. You could've won big.")
        print(balance)





