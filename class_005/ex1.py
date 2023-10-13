# Class 05
#ex1
def middle(x):
    return x[1:-1]

my_list = [1,2,3,4,5,6]
print(middle(my_list))

#ex2
list = [10,20,[300,400,[5000,6000], 500],30,40]
list[2][2].append(7000)
print (list)