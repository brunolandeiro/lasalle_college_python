# Write a computer program that the user enters a positive number and returns a count of 1 to the entered number.
num = -1
while num < 0 :
    num = int(input("Positive Number: "))

for i in range(num) :
    print(i+1)

