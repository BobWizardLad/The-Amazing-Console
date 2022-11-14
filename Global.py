import art
import flagpy as fp

from countryinfo import CountryInfo


art.tprint("Welcome  to  Global")

# Code for user-input
print("Welcome to global! \n Pick a Country")
user_country = input("My country is: ")

art.tprint(user_country)
img = fp.display(user_country)

country = CountryInfo(user_country)
answer = country.capital()

print("What is the capital of " + user_country + "?")
user_guess = input("Answer: ")

if answer == user_guess:
  print("Great job, you got it right!")
else:
    print("You have done " + user_country + " wrong.")










