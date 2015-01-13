#Sean Nicholls
#08/01/2015
#Bubble Sort

def bubble_sort(List):
    swap = True 
    while swap:
        counter = 0
        swap = False
        while counter < len(List)-1:
            if List[counter] > List[counter+1]:
                temp = List[counter+1]
                List[counter+1] = List[counter]
                List[counter] = temp
                counter = counter + 1
                swap = True
            else:
                counter = counter + 1
                swap = False
                           
#Main Program
List = ["Amin","Sam","Sean","Ashley","Henry","Marc"]
bubble_sort(List)
print(List)
