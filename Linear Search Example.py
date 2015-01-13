#Sean Nicholls
#08/01/2015
#Linear Search

def LinearSearch(names, Search):
    found = False
    counter = 0
    while not found and counter < len(names):
        if names[counter] == Search:
            found = True
        else:
            counter = counter+1
    return found

#Main Program


names = ["Sean","Marc","Henry","Amin","Ashley","Toby","Connor"]
Search = input("Who am I looking for?: ")
found = LinearSearch(names, Search)
if found:
    print("Found")
else:
    print("Not Found")
                  
