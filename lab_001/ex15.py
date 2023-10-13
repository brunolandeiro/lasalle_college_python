# 15) Write a Python program to add two given lists and find the sum 
# and difference between the lists. Return the result in a tuple.

list1 = [1,2,3,4,5,6]
list2 = [6,5,4,3]

sum = list1 + list2
diff = list1
for l2 in list2:
    if(diff.count(l2) > 0):
        diff.pop(diff.index(l2))

print(tuple(sum))
print(tuple(diff))

# ver o gabarito