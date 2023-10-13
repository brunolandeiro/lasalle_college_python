#  Given a string and an int n, remove the characters from the string in
# starting from zero to n and returning a new string

text = input("Enter a text: ")
n = int(input("Enter an integer: "))
text2 = text[n:]
print(text2)