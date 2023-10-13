# 19) Create a function that receives a list as a parameter and  returns the second highest value.

def ex19(mylist):
    mylist.sort()
    return mylist[len(mylist)-2]

print(ex19([8,1,2,4,3,5,9,6,3]))
