#Variables
print("\nVariables")
my_var = "Bruno"
print(my_var, type(my_var))
my_var = 10
print(my_var, type(my_var))
my_var = 122.42
print(my_var, type(my_var))

name = "Bruno"
height = 1.70
weight = 75
bmi = weight / (height * height)
print("Hello " + name + " your BMI is: " + str(round(bmi, 2)))