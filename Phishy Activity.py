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
        print("Phising Email here")
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
        print("Safe Email here")
        print("")
        print("---------------------------------------------------------")

        userInput = input("Is this phising? Y or N :  ")

        if userInput == 'y' or userInput == 'Y':
            print("Good try, but this email is safe")
            email3(score)

        elif userInput == 'n' or userInput == 'N':
            score += 1
            print("Good catch! Your new score is: " + str(score))

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