#!/usr/bin/python
import random
class Dice:
    y = '0'
    def roll(self):   
        try: x = int(input("Pick a number between 1 and 6:")) 
        except ValueError:
            d = Dice()
            d.altRoll()
        global y
        y = random.randint(1,6)

        if(x == y):
            print("Yay! You guessed correctly!")
            d = Dice()
            d.altRoll2
        elif(x != y):
            print("Wrong!")
            d = Dice()
            d.altRoll2()
        else:
            d = Dice()
            d.altRoll() 
            

    def altRoll(self):
        try: x = int(input("Not a number, try again:"))
        except ValueError:
            d = Dice()
            d.altRoll()
        global y

        if(x == y):
            print("Yay! You guessed correctly")
            exit()
        else:
            d = Dice()
            d.roll()

    def altRoll2(self):
        try: repeat = input("Wanna try again? (y/n):")
        except ValueError:
            if repeat.lower().startswith("y"):
                d = Dice()
                d.roll() 
            else:
                exit()
         

d = Dice()
d.roll()           

    
