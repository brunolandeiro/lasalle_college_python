# Write a program that asks the user for 4 numbers and returns the result of the following formula:
# 𝑜𝑢𝑡𝑝𝑢𝑡=𝑛𝑢𝑚1∗(𝑛𝑢𝑚2−𝑛𝑢𝑚3)/𝑛𝑢𝑚4

number1 = float(input("Number 1: "))
number2 = float(input("Number 2: "))
number3 = float(input("Number 3: "))
number4 = 0

while number4 == 0:
    number4 = float(input("Number 4 (can not be 0): "))

output = ( number1 * ( number2 - number3) ) / number4
print('𝑜𝑢𝑡𝑝𝑢𝑡: {}'.format(𝑜𝑢𝑡𝑝𝑢𝑡))