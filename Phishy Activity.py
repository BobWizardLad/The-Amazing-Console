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


    def email1(score):
        print("Phising Email here")
        print("")

        userInput = input("Is this phising? Y or N :  ")

        if userInput == 'y' or 'Y':
            score += 1
            print("Good catch! Your new score is: " + score)

        elif userInput == 'n' or 'N':
            print("Good try, but this email is phising")

        else:
            print("That wasn't an option, try tht again")
            email1()

    #Email 2 - safe


    #Email 3 - phising

    #Funtion call
    email1(score)

    pass

phishy()