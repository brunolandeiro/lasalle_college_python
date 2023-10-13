# Write a program in python that receives from the user two values and save in different 
# variables. Switch the values of the variables and print them at the end.
#  Ex: Var1 = 4 and Var2 = 6
#  print(var1) –> 6 and print(var2) -> 4
var1 = input("Enter var1: ")
var2 = input("Enter var2: ")
var_aux = var2
var2 = var1
var1 = var_aux
print("var1 = ", var1)
print("var2 = ", var2)