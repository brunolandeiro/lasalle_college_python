# Write a function (isContain) that receives an array of size 10 and a digit and returns if that digit is in the array content.

def isContain(array_of_10, num):
    contain = False
    for x in array_of_10 :
        if(x == num):
            contain = True
    return contain

array_of_10 = [1,2,3,4,5,6,7,8,9,10]
num = 3
print('{} contains the element {}? {}'.format(array_of_10, num, isContain(array_of_10, num)))

