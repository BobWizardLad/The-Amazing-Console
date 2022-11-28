# Import your files here!
import art
import time
import lucky
import phishy_activity
import TurtleRace
import Global
import monkay_maze
import secret

# Menu text for selection
def getMenu():
    print("1. Cyber")
    print("2. Race")
    print("3. Find X")
    print("4. Luck")
    print("5. Secret")
    print("6. Fish")
    print("7. Global")
    print("8. Ladybug")
    print("Type 1-8 in the console to launch a prompt, or 0 to quit")

#---------- Main progression starts here ----------

# Title card
art.tprint("Welcome to The Amazing Console!")

# Prompts
print("The prompts for this console are...")
time.sleep(3)

# Give options
end = 0
while(end != 1):
    getMenu()
    user_in = input("I Choose: ")

    if(user_in.isnumeric):
        if user_in == "1":
            print("404: Not Found")
        elif user_in == "2":
            TurtleRace.Race()
        elif user_in == "3":
            monkay_maze.findx_main()
        elif user_in == "4":
            lucky.teamLuck()
        elif user_in == "5":
            secret.pegasus()
        elif user_in == "6":
            phishy_activity.phishy()
        elif user_in == "7":
            Global.global_main()
        elif user_in == "8":
            print("404: Not Found")
        elif user_in == "0":
            end = 1
            print("Goodbye!")

