#  Given a list of ints, return True if the first and last numbers in a list are identical.

list1 = [1,2,3,4]
list2 = [1,1,1]
list3 = [1]

def ex5(list_ints):
    return list_ints[0] == list_ints[-1]

print(ex5(list1))
print(ex5(list2))
print(ex5(list3))