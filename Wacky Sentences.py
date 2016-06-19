#Made by Hunter1471(hunt3r1471@gmail.com)
#Start 
import random
from random import randint
possibilities1 = 6
possibilities2 = 26
possibilities3 = 26
possibilities4 = 26
totalpossibilities = possibilities1*possibilities2*possibilities3*possibilities4

#Intro
print("Welcome to Wacky Sentences! There are currently"+" "+str(totalpossibilities)+" "+"sentence possibilities!")

#First Word
random1 = randint(1,possibilities1)
if (random1==1):
    a="My"
elif (random1==2):
    a="Your"
elif (random1==3):
    a="His"
elif (random1==4):
    a="Her"
elif (random1==5):
    a="Their"
else:
    a="A"

#Second Word
random2 = randint(1,possibilities2)
if (random2==1):
    b="apple"
elif (random2==2):
    b="banana"
elif (random2==3):
    b="cat"
elif (random2==4):
    b="dog"
elif (random2==5):
    b="elephant"
elif (random2==6):
    b="frog"
elif (random2==7):
    b="giraffe"
elif (random2==8):
    b="house"
elif (random2==9):
    b="igloo"
elif (random2==10):
    b="jam"
elif (random2==11):
    b="kale"
elif (random2==12):
    b="lamb"
elif (random2==13):
    b="mongoose"
elif (random2==14):
    b="naan"
elif (random2==15):
    b="oats"
elif (random2==16):
    b="panda"
elif (random2==17):
    b="quad bike"
elif (random2==18):
    b="rope"
elif (random2==19):
    b="swan"
elif (random2==20):
    b="toad"
elif (random2==21):
    b="umbrella"
elif (random2==22):
    b="volleyball"
elif (random2==23):
    b="wand"
elif (random2==24):
    b="xylophone"
elif (random2==25):
    b="yarn"
else:
    b="zebra"

#Third Word
random3 = randint(1,possibilities3)
if (random3==1):
    c="ate"
elif (random3==2):
    c="boiled"
elif (random3==3):
    c="cried about"
elif (random3==4):
    c="drank"
elif (random3==5):
    c="earned"
elif (random3==6):
    c="fought"
elif (random3==7):
    c="groaned about"
elif (random3==8):
    c="hated"
elif (random3==9):
    c="ignited"
elif (random3==10):
    c="joined"
elif (random3==11):
    c="killed"
elif (random3==12):
    c="loved"
elif (random3==13):
    c="made"
elif (random3==14):
    c="navigated"
elif (random3==15):
    c="opened"
elif (random3==16):
    c="played football with"
elif (random3==17):
    c="queued for"
elif (random3==18):
    c="rode"
elif (random3==19):
    c="swam in"
elif (random3==20):
    c="tamed"
elif (random3==21):
    c="underestimated"
elif (random3==22):
    c="volleyed"
elif (random3==23):
    c="washed"
elif (random3==24):
    c="x-rayed"
elif (random3==25):
    c="yanked"
else:
    c="zapped"
    
#Fourth Word
random4 = randint(1,possibilities4)
if (random4==1):
    d="a potato"
if (random4==2):
    d="bogies"
if (random4==3):
    d="chocolate"
elif (random4==4):
    d="dragons"
if (random4==5):
    d="ethernet cables"
if (random4==6):
    d="fish"
if (random4==7):
    d="goslings"
if (random4==8):
    d="home runs"
if (random4==9):
    d="ice"
if (random4==10):
    d="jaguars"
if (random4==11):
    d="ketchup"
if (random4==12):
    d="lollipops"
elif (random4==13):
    d="Mountain Dew"
if (random4==14):
    d="names"
if (random4==15):
    d="ostriches"
if (random4==16):
    d="plants"
if (random4==17):
    d="quacks"
if (random4==18):
    d="RAM"
if (random4==19):
    d="soap"
if (random4==20):
    d="towels"
if (random4==21):
    d="unicode"
if (random4==22):
    d="varnish"
if (random4==23):
    d="walk"
if (random4==24):
    d="xenon"
if (random4==25):
    d="Yale"
else:
    d="Zambia"

#Printing the Sentence
print(a+" "+b+" "+c+" "+d+".")

#End Script

      
