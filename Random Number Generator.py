#Made by Hunter1471 (hunt3r1471@gmail.com)
#Imports
import random
from random import randint

#Intro
print("Welcome to the Random Number Generator!")

#Maximum Number
inputnumber = input("Which number would you like to go up to?")
maxnumber = int(inputnumber)

#Times Random Numbers Are Generated
times = input("How many numbers do you want to generate within the range?")
times = int(times)

#Printing
for i in range(times):
    randomnumber = print(randint(1,maxnumber))
