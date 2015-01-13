#Sean Nicholls
#List Development Exercise 2

import random

def question_asker(countries, capitals):
    score = 0
    counter = 1
    while counter <=5:
        selector = random.randint(0, 9)
        country = countries[selector]
        capital = capitals[selector]
        userguess = input("Where is the capital of {0}? ".format(country))
        if userguess == capital:
            score = score + 1
            print("That is correct well done")
        else:
            print("That is incorrect")
        counter = counter + 1
    return score

#main program
countries = ["England","Scotland","Spain","Portugal","Germany","Italy","France","Netherlands","Greece","Poland"]
capitals = ["London","Edinburgh","Madrid","Lisbon","Berlin","Rome","Paris","Amsterdam","Athens","Warsaw"]
score = question_asker(countries, capitals)
print("You scored {0} out of 5".format(score))
