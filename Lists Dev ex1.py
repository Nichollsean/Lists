#Sean Nicholls
#List Development Exercise 1

import random

countries = ["England","Scotland","Spain","Portugal","Germany","Italy","France","Netherlands","Greece","Poland"]
capitals = ["London","Edinburgh","Madrid","Lisbon","Berlin","Rome","Paris","Amsterdam","Athens","Warsaw"]
selector = random.randint(0, 9)
country = countries[selector]
capital = capitals[selector]
userguess = False
while userguess == False:
    userguess = input("Where is the capital of {0}? ".format(country))
    if userguess == capital:
        userguess = True
        print("That is correct well done")
    else:
        userguess = False
        print("Please try again")
        
