# 20) Write a Python program to return a new set with unique 
# elements from both sets by removing duplicates.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1)
print(set2)
set3 = set(list(set1) + list(set2))
print(set3)
