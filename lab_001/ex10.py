# 10) Write a function that takes a list of numbers stored in ascending 
# order and two values ( lower limit and upper limit), and displays the 
# sublist whose items are greater than or equal to the lower limit and 
# less than or equal to the upper limit.
# Example: initial list=[12,14,15,16,18,20,24,26,28,32,34,38]
# lower limit=13
# upper limit=26
# displayed list: [14,15,16,18,20,24,26]

def ex10 (my_list, min, max):
    sublist = []
    for i in my_list:
        if i >= min and i <= max:
            sublist.append(i)
    print(sublist)


list=[12,14,15,16,18,20,24,26,28,32,34,38]
lower_limit=13
upper_limit=26
ex10(list, lower_limit, upper_limit)