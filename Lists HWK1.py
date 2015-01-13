
#Sean Nicholls
#Lists HWK1

def table(name1,name2,name3,name4,name5,name6,name7,name8):    
    print(" 1. {0}".format(name1))
    print(" 2. {0}".format(name2))
    print(" 3. {0}".format(name3))
    print(" 4. {0}".format(name4))
    print(" 5. {0}".format(name5))
    print(" 6. {0}".format(name6))
    print(" 7. {0}".format(name7))
    print(" 8. {0}".format(name8))
    print(" 0. Exit program")

#mainprogram
    
name1 = input("Please enter the name of the first student: ")
name2 = input("Please enter the name of the second student: ")
name3 = input("Please enter the name of the third student: ")
name4 = input("Please enter the name of the fourth student: ")
name5 = input("Please enter the name of the fifth student: ")
name6 = input("Please enter the name of the sixth student: ")
name7 = input("Please enter the name of the seventh student: ")
name8 = input("Please enter the name of the eighth student: ")

table(name1,name2,name3,name4,name5,name6,name7,name8)

selection = int(input("Please select a student to edit: "))

if selection == 1:
    name1 = input("Please enter their new name: ")
    print("Here is the new table")
    table(name1,name2,name3,name4,name5,name6,name7,name8)
elif selection == 2:
    name2 = input("Please enter their new name: ")
    print("Here is the new table")
    table(name1,name2,name3,name4,name5,name6,name7,name8)
elif selection == 3:
    name3 = input("Please enter their new name: ")
    print("Here is the new table")
    table(name1,name2,name3,name4,name5,name6,name7,name8)
elif selection == 4:
    name4 = input("Please enter their new name: ")
    print("Here is the new table")
    table(name1,name2,name3,name4
          ,name5,name6,name7,name8)
elif selection == 5:
    name5 = input("Please enter their new name: ")
    print("Here is the new table")
    table(name1,name2,name3,name4,name5,name6,name7,name8)
elif selection == 6:
    name6 = input("Please enter their new name: ")
    print("Here is the new table")
    table(name1,name2,name3,name4,name5,name6,name7,name8)
elif selection == 7:
    name7 = input("Please enter their new name: ")
    print("Here is the new table")
    table(name1,name2,name3,name4,name5,name6,name7,name8)
elif selection == 8:
    name8 = input("Please enter their new name: ")
    print("Here is the new table")
    table(name1,name2,name3,name4,name5,name6,name7,name8)
else:
    print("Program closed")
