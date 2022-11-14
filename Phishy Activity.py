def phishy():
    print("---------------------------------------------------------")
    print("You Have chosen the fishing tab... oh. I mean Phising tab")
    print("")
    print("This task includes deciding weather an email that is given to you phising or safe.")
    print("---------------------------------------------------------")
    print("The first email is coming up, DON'T GET PHISHED")
    print("")
    print("We'll be keeping score. Current Score: 0")
    print("---------------------------------------------------------")


    score = 0


    #Email 3 - phising
    def email3(score):
        print("From: kngPrnceCharming@money.com")
        print("To: wyatt@marsiglio.com")
        print("Subject: SEND MONEY NOW!!!!1!")
        print("")
        print(" Helo! I am a sri lankan prince from Sri Lanka. I need a small lone of money, then I will triple it")
        print(" u in gold. Send $1000 dollars money to $189471 cash app, and I will triple investment.")
        print("")
        print(" -Sri Lanka Prince Charming")

        print("")
        print("---------------------------------------------------------")

        userInput = input("Is this phising? Y or N :  ")

        if userInput == "y" or userInput == "Y":
            score += 1
            print("Good catch! Your final score is: " + str(score))

        elif userInput == "n" or userInput == "N":
            print("Good try, but this email is phising")

        else:
            print("That wasn't an option, try tht again")
            email3(score)

    # Email 2 - safe
    def email2(score):
        print("From: JohnFinance@BankOfAmerica.com")
        print("To: wyatt@marsiglio.com")
        print("Subject: Confirm Purchase")
        print("")
        print(" Hello Wyatt, we noticed that you purchased a Dunk Tank for $6,500, and 250 double packs of pickle ")
        print(" juice for $7,500, on amazon.com. If you did not make this purchase please contact us either by calling,")
        print(" emailing, or coming into our facility.")
        print("")
        print(" John Finance, Bank of America")
        print("")
        print("---------------------------------------------------------")

        userInput = input("Is this phising? Y or N :  ")

        if userInput == 'y' or userInput == 'Y':
            print("Good try, but this email is safe")
            email3(score)

        elif userInput == 'n' or userInput == 'N':
            score += 1
            print("---------------------------------------------------------")
            print("Good catch! Your new score is: " + str(score))
            print("")
            print("Here comes the next email")
            print("---------------------------------------------------------")
            email3(score)

        else:
            print("That wasn't an option, try tht again")
            email2(score)

    #Email 1 - safe
    def email1(score):
        print("Subject: FREE CHESS MEMBERSHIP")
        print("From: welcome@chess.com")
        print("To: wyatt@marsiglio.com")
        print(" Yo Chessmaster!")
        print(" As you know we have a sweet subscription called chess premium. This subscription allows you to access")
        print(" new videos and terms in chess with NO ADS! 1 term you may not know applies to chess is crissaunt this")
        print(" meaning is where you take your knight and move them in a “C’ pattern because this looks like a")
        print(" crussaunt and will allow you to take multiple pieces and help you in the long run! SUBSCRIBe FOR MORe!")
        print(" Click buttun bellow and make sure your credentalls qualify for the new discounted version of chess")
        print(" premium! click bellow for detales!")
        print(" Chass-com-not-a-scam.html")
        print("")
        print("---------------------------------------------------------")

        userInput = input("Is this phising? Y or N :  ")

        if userInput == "y" or userInput == "Y":
            score += 1
            print("---------------------------------------------------------")
            print("Good catch! Your new score is: " + str(score))
            print("")
            print("Here comes the next email")
            print("---------------------------------------------------------")
            email2(score)
        elif userInput == "n" or userInput == "N":
            print("Good try, but this email is phising")
            email2(score)

        else:
            print("That wasn't an option, try tht again")
            email1(score)

    #Funtion call
    email1(score)

phishy()
