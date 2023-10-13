# 14) Given an input string, count the occurrences of all 
# characters in a string.
# Example: Input: ‘ pynativepynvepynative ‘
# Sortie: {'p': 3, 'y': 3, 'n': 3, 'a': 2, 't': 2, 'i': 2, ' v': 3, 'e': 3}

input = "pynativepynvepynative"
input_as_list = []
sortie = {}
for i in input: 
    input_as_list.append(i)

input_as_set = set(input_as_list)

for i in input_as_set:
    sortie[i] = input_as_list.count(i)

print(sortie)

#Should do without the list 

