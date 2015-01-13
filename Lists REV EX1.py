#Sean NIcholls
#Lists REV EX1

names = []
counter = 1
for count in range(6):
    name = input("Please enter name {0}: ".format(counter))
    names.append(name)
    counter = counter + 1

place_holder = ("Place")
names.insert(1
             ,place_holder)
range_low = int(input("What is the first name you wish to view: "))
range_high = int(input("What is the last name you wish to view: "))
print("Here are the names you requested {0}".format(names[range_low,range_high]))
