#Based off http://suyeon-son.com/sandbox/mad-libs.html
print("Welcome to the Excuses, Excuses Storyteller!")

#Names
randomname = input("Create a random name (e.g Alex):")
name = input("What is your name?:")

#Nouns
snoun1 = input("Submit a singular noun (e.g Book):")
snoun2 = input("Submit another singular noun (e.g Computer):")
plnoun1 = input("Submit a plural noun (e.g Pencils):")
plnoun2 = input("Submit another plural noun (e.g Pens):")
animal = input("Give me the name of any animal (e.g Dog):")
prnoun = input ("Give me the name of a proper noun (e.g Domino's):")

#Adjectives
adj1 = input("Give me the name of an adjective (e.g Wonderful):")
adj2 = input("Give me the name of another adjective (e.g Weird):")
adj3 = input("Give me the name of another adjective (e.g Angry):")
adj4 = input("Give me the name of another adjective (e.g Happy):")
disgusting = input("Type in the name of a disgusting object (e.g Bugs):")

#Verbs
pastverb1 = input("Submit a verb in the past tense (e.g Poked):")
pastverb2 = input("Submit another verb in the past tense(e.g Found):")
pastverb3 = input("Submit a verb in the past tense(e.g Wrote):")
presentverb = input("Submit a verb in the present tense:(e.g Found)")

#Occupation
occupation = input("Give me the name of any occupation(e.g Janitor):")

#Superlative
superlative = input("Submit a superlative (e.g Worst):")

#Print Story
print("To: "+randomname+"@email.com")
print("From: "+name+"@email.com")
print("Subject: Can't make work today")
print(" ")
print("Hi,")
print(" ")
print("I've come down with a bad case of the "+disgusting+".")
print("I've been throwing up "+plnoun1+" all day and keep forgetting what "+plnoun2+" are. My hands are "+adj1+" as a result, and my hair is "+adj2+".")
print("Yesterday, I was bitten by my neighbor's  "+animal+". I tried to fight it with my "+snoun1+", but it "+pastverb1+" and proceeded to furiously "+presentverb+".")
print("I "+pastverb2+" and called for help, but only a "+occupation+" came to my aid. He was "+adj4+". I finally reached my phone and dialed 911, but for some")
print("reason it redirected me to "+prnoun+"! It was a lost cause. I "+pastverb3+" all the way back home, where I found solace in my "+snoun2+". I'm sorry to say, ")
print("but I won't make it into work today. Hopefully you will understand.")

print("Sincerely,")
print("Your "+superlative+" employee.")
