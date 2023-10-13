# 6) Given a list of two. Create a third list by choosing an item odd index in the first list 
# and even index in the second.
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
list3 = []

for i in range(0,len(listOne)):
    if(i % 2 == 0):
        list3.append(listTwo[i])
    else:
        list3.append(listOne[i])

print(list3)
