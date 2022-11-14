print("Welcome to the CASINO")
print("Lets go get some MONEY$$$. SHEEESH")
global balance
balance = 1000
print("Your starting balance is", balance)
print("Your goal is to get to 2,000")

import random
wordlist = ["Banana", "Apples", "Grapes", "7up", "Sheesh", "LIL JOSH", "Yung Alton", "LudaChris", "Snickers"]

def slotmachine():
    global balance
    n = 0
    slotlist = []
    while (n < 3):

        x = random.randint(1,len(wordlist))
        slotlist += [x]
        n += 1
    nonrepeatslotlist = (slotlist)
    if len(nonrepeatslotlist) == 1:
        print("YOU WIN")
        balance += 1000
    else:
        print("Did you know that 99% of gamblers quit before their first big win?")
        balance -= 250
    print(slotlist)

slotmachine()


