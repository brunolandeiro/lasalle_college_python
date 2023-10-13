# 7) Given an input list, remove the element at index 4 and add it at the 2nd position and also, at the end of the list.
List = [54, 44, 27, 79, 91, 41]

element_at_index4 = List.pop(4)
List = List[0:1] + [element_at_index4] + List[1:] + [element_at_index4]
print(List)

# OR
List = [54, 44, 27, 79, 91, 41]

element_at_index4 = List.pop(4)
List.insert(1, element_at_index4)
List.append(element_at_index4)
print(List)