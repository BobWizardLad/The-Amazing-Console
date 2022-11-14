def slotMachine(balance):
    import random
    wordList = ["Banana", "Apples", "Grapes", "7up", "Sheesh", "LIL JOSH", "Dr. Chandra", "Yung Alton", "LudaChris",
                "Snickers"]
    n = 0
    slotList = []
    while (n < 3):
        x = random.randint(1, len(wordList))
        slotList += [wordList[x]]
        n += 1
    nonRepeatSlotList = (slotList)
    if len(nonRepeatSlotList) == 1:
        print("YOU WIN")
        balance += 1000
    else:
        print("Did you know that 99% of gamblers quit before their first big win?")
        balance -= 250
    print(slotList)
def teamLuck(balance):
    print("Welcome to the CASINO")
    print("Lets go get some MONEY$$$. SHEEESH")
    print("Your starting balance is", balance)
    print("Your goal is to get to 2,000")


    print("Slotmachine? (Y/N)")
    decision = input()

    while (decision == "Y"):
        slotMachine(balance)
        print("Would you like to keep going?")
        decision = input()
    if (decision == "N"):
        print("You are not smart. You could've won big.")

teamLuck(1000)

