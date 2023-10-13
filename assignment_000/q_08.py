# Factorial is a mathematical operation represented by "!" which multiplies the integer predecessors of the number up to 1.
# For example:
# 4! = 4*3*2*1 = 24.
# Exception: 0! = 1.
# Write a computer program that contains a function called "factorial" that returns the factorial of the number entered by the user.
def factorial(x):
    if(x == 0) :
        return 1
    
    result = 1
    for i in range(x) :
        result = result * (i+1)
    return result

num = -1
while num < 0 :
    num = int(input("Positive Number: "))

result = factorial(num)
print('{0}! = {1}'.format(num, result))

