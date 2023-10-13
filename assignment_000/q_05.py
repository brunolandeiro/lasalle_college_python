# 5) We know that a triangle is formed by three sides that have a certain measure. 
# These measures must follow the following rule: 
# | b - c | < a < b + c 
# | a - c | < b < a + c 
# | a - b | < c < a + b
# Write a computer program that takes the 3 sides of a triangle and returns if that triangle exists
def module_of(x):
    if x >= 0 :
        return x
    else :
        return x * (-1)

def is_a_crescent_order(num1, num2, num3):
    return num1 < num2 and num2 < num3

triangle_exist = True
a = float(input("Enter Side A: "))
b = float(input("Enter Side B: "))
c = float(input("Enter Side C: "))
# | b - c | < a < b + c 
rule1 = is_a_crescent_order(module_of (b - c), a, (b + c))
# | a - c | < b < a + c 
rule2 = is_a_crescent_order(module_of (a - c), b, (a + c))
# | a - b | < c < a + b
rule3 = is_a_crescent_order(module_of (a - b), c, (a + b))

if rule1 and rule2 and rule3 :
    print("exists")
else :
    print("do not exists")

#test
# Enter Side A: 50.25
# Enter Side B: 30.5
# Enter Side C: 43.84846
# exists
