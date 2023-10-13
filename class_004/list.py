#List

my_list = [1,2,3,4,5,6]
print(my_list)

my_list = [1, True, "Bruno"]
print(my_list)

for i in range(len(my_list)):
    print(my_list[i], end=" ")
print()

for item in my_list:
    print(item, end=" ")
print()

my_list = [3, 5, 1]
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list = [
    ["Orange", 4.66],
    ["Apple", 2.56],
    ["Milk", 5.55],
    ["Coffee", 3.98]
]

print(my_list)
for item in my_list:
    print(item)

my_list.sort()
print(my_list)

def set_key(item):
    return item[1]

my_list.sort(key=set_key)
print(my_list)

my_list.sort(key=lambda item : item[1])
print(my_list)

my_list_1 = ["a", "b", "c"]
my_list_2 = [1, 2, 3]

my_result = my_list_1 + my_list_2
print(my_result)

#Slice
print(my_result[2:5])
print(my_result[-1])
print(my_result[3:])
print(my_result[:5])

my_result.append("new")
print(my_result)

my_result.insert(2, "new")
print(my_result)

my_result.pop()
print(my_result)

del(my_result[2:4])
print(my_result)

my_result.clear()
print(my_result)

my_result.extend(my_list_1)
print(my_result)