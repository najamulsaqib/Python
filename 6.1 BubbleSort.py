#function to sort list
def sort_lsit(lsit, len):
    for i in range(0, len):
        for j in range(i+1, len):
            if lsit[i] > list[j]:
                #Assigning Values
                list[i] , list[j] = list[j] , list[i]

#Main
list = [32, 13, 12, 15, 18, 1, 43, 11, 27]
len = len(list)
sort_lsit(list, len)
print(list)