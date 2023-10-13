# Write a computer program that the user between one age and the program returns:
# "Child" for ages under 12
# "Young" for ages 12 and under and under 18
# "Adult" for ages 18 and under and under 60
# "Senior" for ages 60 and over.

age = int(input("Enter your age: "))

if age >= 60 :
    output = "Senior"
elif age < 60 and age >=18 :
    output = "Adult"
elif age < 18 and age >=12 :
    output = "Young"
elif age < 12 :
    output = "Child"

print(output)