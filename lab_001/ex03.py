# Given a string of odd length greater than 7, 
# flip a string composed of the three characters in the middle of a given string

txt_list = []
text = input("Enter a string of odd length greater than 7: ")
for character in text:
    txt_list.append(character)

text_lenth = len(text)
print("text_lenth: ", text_lenth)
middle_index = int(text_lenth/2)
print("middle_index: ", middle_index)
print("middle_value - 1:\t", text[middle_index-1])
print("middle_value:\t", text[middle_index])
print("middle_value + 1:\t", text[middle_index+1])

txt_list[middle_index-1], txt_list[middle_index+1] = txt_list[middle_index+1], txt_list[middle_index-1]

text = ""
for i in txt_list:
    text += i

print(text)

