# Import libraries
import art
import flagpy as fp
from countryinfo import CountryInfo

# Tprint for print text
art.tprint("Welcome  to  Global!")

# Code for user-input
print("Welcome to global! \n Pick a Country")
user_country = input("My country is: ")

# Setting up and defining correct answers
art.tprint(user_country)
img = fp.display(user_country)
country = CountryInfo(user_country)
answer = country.capital()
answerTwo = country.region()

# Question One
print("What is the capital of " + user_country + "?")
print()
user_guess = input("Answer: ")

# Determining if answer is correct or false
if answer == user_guess:
  print("Great job, you got it right! 😃")
else:
    print("Incorrect!")

# Question Two
print()
print("What continent is " + user_country + " in?")
user_guess_two = input("Answer: ")

if user_guess_two == answerTwo:
    print("Correct! 😃")
else:
    print("Incorrect!")










