# 16) Write a Python program to reverse a given string.

text = "Bruno Lemos Landeiro"
text_reverse = ""

for i in reversed(range(len(text))):
    text_reverse += text[i]

print(text_reverse)

#or
text = "Bruno Lemos Landeiro"
text_reverse = ""

for i in range(len(text)-1,-1,-1):
    text_reverse += text[i]

print(text_reverse)

#or
print(text[::-1])

