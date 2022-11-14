def phishy():
    print("You Have chosen the fishing tab... oh. I mean Phising tab")
    print("Good luck")
    print("")
    print("This task includes deciding weather an email that is given to you phising or safe.")
    print("")
    print("")
    print("The first email is coming up, DON'T GET PHISHED")
    print("We'll be keeping score. Current Score: 0")

    score = 0


    #Email 3 - phising
    def email3(score):

        print("Phising Email here")
        print("")

        userInput = input("Is this phising? Y or N :  ")

        if userInput == 'y' or 'Y':
            score += 1
            print("Good catch! Your final score is: " + score)

        elif userInput == 'n' or 'N':
            print("Good try, but this email is phising")

        else:
            print("That wasn't an option, try tht again")
            email3(score)

    # Email 2 - safe
    def email2(score):
        print("Safe Email here")
        print("")

        userInput = input("Is this phising? Y or N :  ")

        if userInput == 'y' or 'Y':
            print("Good try, but this email is safe")

        elif userInput == 'n' or 'N':
            score += 1
            print("Good catch! Your new score is: " + score)

            print("")
            print("Here comes the next email")
            print("")
            email3(score)

        else:
            print("That wasn't an option, try tht again")
            email2(score)

    #Email 1 - safe
    def email1(score):
        print("Phising Email here")
        print("")

        userInput = input("Is this phising? Y or N :  ")

        if userInput == 'y' or 'Y':
            score += 1
            print("Good catch! Your new score is: " + score)

            print("")
            print("Here comes the next email")
            print("")
            email2(score)
        elif userInput == 'n' or 'N':
            print("Good try, but this email is phising")

        else:
            print("That wasn't an option, try tht again")
            email1(score)

    #Funtion call
    email1(score)

    pass

phishy()