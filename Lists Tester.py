#Sean Nicholls
#06/01/15
#Lists Trial

k1llmAchine = ["k1llmAchine","51","49"]
bob7424 = ["bob7424","5","99"]
hAxOr12 = ["hAxOr12","72","30"]

table = [k1llmAchine,bob7424,hAxOr12]

print("{0:<14}{1:<2}".format("Name", "K:D"))
count = 0
for each in table:
    print("|{0:<13}{1}{2:<1}:{3}".format(table[count][0],"|",table[count][1],table[count][2]))
    count = count + 1
    

    

